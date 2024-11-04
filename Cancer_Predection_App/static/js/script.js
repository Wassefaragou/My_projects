function submitForm() {
    const data = {
        'Clump Thickness': parseInt(document.getElementById('clump_thickness').value),
        'Uniformity of Cell Size': parseInt(document.getElementById('cell_size').value),
        'Uniformity of Cell Shape': parseInt(document.getElementById('cell_shape').value),
        'Marginal Adhesion': parseInt(document.getElementById('marginal_adhesion').value),
        'Single Epithelial Cell Size': parseInt(document.getElementById('epithelial_cell_size').value),
        'Bare Nuclei': parseInt(document.getElementById('bare_nuclei').value),
        'Bland Chromatin': parseInt(document.getElementById('bland_chromatin').value),
        'Normal Nucleoli': parseInt(document.getElementById('normal_nucleoli').value),
        'Mitoses': parseInt(document.getElementById('mitoses').value)
    };

    // Clear previous error message
    const errorMessage = document.getElementById('errorMessage');
    errorMessage.style.display = 'none';
    errorMessage.innerText = '';

    // Check for empty inputs
    for (const key in data) {
        if (isNaN(data[key]) || data[key] < 0) {
            errorMessage.innerText = 'Please enter valid numbers for all fields.';
            errorMessage.style.display = 'block'; // Show the error message
            return; // Exit the function if there's an invalid input
        }
    }

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const resultModal = document.getElementById('resultModal');
        const resultContent = document.getElementById('resultContent');
        
        // Display the prediction result in the modal
        resultContent.innerText = `Prediction: ${data.prediction}`;
        resultModal.style.display = 'flex';
    })
    .catch(error => console.error('Error:', error));
}


// Function to check the API status
function checkApiStatus() {
    // Send GET request to status endpoint
    fetch('/status')
    .then(response => {
        if (response.ok) {
            document.getElementById('statusResult').innerText = 'API is Online';
            document.getElementById('statusResult').classList.add("status-box");
        } else {
            document.getElementById('statusResult').innerText = 'API is Offline';
            document.getElementById('statusResult').classList.add("status-box");
        }
    })
    .catch(() => {
        document.getElementById('statusResult').innerText = 'API is Offline';
        document.getElementById('statusResult').classList.add("status-box");
    });
}


function toggleMenu() {
            const navLinks = document.querySelector('.nav-links');
            navLinks.classList.toggle('active');
            }