const imageInput = document.getElementById("imageInput");
const uploadBtn = document.getElementById("uploadBtn");
const preview = document.getElementById("preview");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const vehicleNumber = document.getElementById("vehicleNumber");
const brightness = document.getElementById("brightness");
const blur = document.getElementById("blur");
const duplicate = document.getElementById("duplicate");
const status = document.getElementById("status");

function resetResultCards() {
    vehicleNumber.textContent = "--";
    brightness.textContent = "--";
    blur.textContent = "--";
    duplicate.textContent = "--";
    status.textContent = "--";
    result.hidden = true;
}

function showPreview(file) {
    if (!file || !file.type.startsWith("image/")) {
        return;
    }

    const reader = new FileReader();

    reader.onload = (event) => {
        preview.innerHTML = `<img src="${event.target.result}" alt="Selected vehicle preview">`;
    };

    reader.readAsDataURL(file);
}

imageInput.addEventListener("change", (event) => {
    const file = event.target.files[0];
    showPreview(file);
    resetResultCards();
});

uploadBtn.addEventListener("click", async () => {
    const file = imageInput.files[0];

    if (!file) {
        alert("Please select an image first.");
        return;
    }

    loading.style.display = "block";
    uploadBtn.disabled = true;
    uploadBtn.textContent = "Analyzing...";
    resetResultCards();

    try {
        const formData = new FormData();
        formData.append("file", file);

        const uploadResponse = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        if (!uploadResponse.ok) {
            throw new Error("Upload failed.");
        }

        const uploadData = await uploadResponse.json();
        const id = uploadData.processing_id;

        let currentStatus = "pending";

        while (currentStatus !== "completed" && currentStatus !== "failed") {
            const statusResponse = await fetch(`/status/${id}`);
            const statusData = await statusResponse.json();
            currentStatus = statusData.status;

            if (currentStatus === "completed" || currentStatus === "failed") {
                break;
            }

            await new Promise((resolve) => setTimeout(resolve, 1000));
        }

        const resultResponse = await fetch(`/result/${id}`);
        const resultData = await resultResponse.json();

        if (resultData.status === "failed") {
            throw new Error(resultData.failure_reason || "Analysis failed.");
        }

        const analysis = JSON.parse(resultData.result);

        vehicleNumber.textContent = analysis.vehicle_number || "Not found";
        brightness.textContent = `${analysis.brightness.status} (${analysis.brightness.value})`;
        blur.textContent = `${analysis.blur.status} (${analysis.blur.score})`;
        duplicate.textContent = analysis.duplicate ? "Duplicate" : "Unique";
        status.textContent = analysis.valid_plate ? "✅ Valid Plate" : "❌ Invalid Plate";
        result.hidden = false;
    } catch (error) {
        vehicleNumber.textContent = "Error";
        brightness.textContent = "--";
        blur.textContent = "--";
        duplicate.textContent = "--";
        status.textContent = error.message;
        result.hidden = false;
    } finally {
        loading.style.display = "none";
        uploadBtn.disabled = false;
        uploadBtn.textContent = "Analyze Image";
    }
});