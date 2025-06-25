// Global state
let activeTab = 'register';
let focusedField = null;
let showPassword = false;

// Tab switching functionality
function switchTab(tab) {
    activeTab = tab;

    // Update tab buttons
    document.getElementById('register-tab').classList.toggle('active', tab === 'register');
    document.getElementById('signin-tab').classList.toggle('active', tab === 'signin');

    // Update form visibility
    document.getElementById('register-form').classList.toggle('active', tab === 'register');
    document.getElementById('signin-form').classList.toggle('active', tab === 'signin');
}

// Input focus handling
function handleFocus(fieldId) {
    focusedField = fieldId;
    updateFloatingLabel(fieldId);
}

// Input blur handling
function handleBlur(fieldId) {
    const input = document.getElementById(fieldId);
    if (!input.value.trim()) {
        focusedField = null;
    }
    updateFloatingLabel(fieldId);

    // Show email error if email field is empty after blur
    if (fieldId === 'id_email' && input.value.trim() && !isValidEmail(input.value)) {
        showError('email');
    } else {
        hideError('email');
    }
}

// Input change handling
function handleInput(fieldId) {
    updateFloatingLabel(fieldId);

    // Hide error messages when user starts typing
    if (fieldId === 'id_email') {
        hideError('email');
    }
}

// Update floating label position
function updateFloatingLabel(fieldId) {
    const input = document.getElementById(fieldId);
    const label = document.querySelector(`label[for="${fieldId}"]`);

    if (!input || !label) return;

    const isActive = focusedField === fieldId || input.value.trim() || input.type === 'select-one';
    label.classList.toggle('active', isActive);
}

// Password visibility toggle
function togglePassword() {
    showPassword = !showPassword;
    const passwordInput = document.getElementById('password');
    const eyeIcon = document.getElementById('eye-icon');
    const eyeOffIcon = document.getElementById('eye-off-icon');

    passwordInput.type = showPassword ? 'text' : 'password';
    eyeIcon.classList.toggle('hidden', showPassword);
    eyeOffIcon.classList.toggle('hidden', !showPassword);
}

// Email validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Show error message
function showError(fieldId) {
    const errorElement = document.getElementById(`${fieldId}-error`);
    if (errorElement) {
        errorElement.classList.add('show');
    }
}

// Hide error message
function hideError(fieldId) {
    const errorElement = document.getElementById(`${fieldId}-error`);
    if (errorElement) {
        errorElement.classList.remove('show');
    }
}

// Initialize the page
document.addEventListener('DOMContentLoaded', function () {
    // Set initial state for country select (always has a value)
    updateFloatingLabel('country');

    // Add event listeners for form submission
    document.querySelector('.create-account-btn').addEventListener('click', function (e) {
        e.preventDefault();

        if (activeTab === 'register') {
            // Validate registration form
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();

            let hasErrors = false;

            if (!email || !isValidEmail(email)) {
                showError('email');
                hasErrors = true;
            }

            if (!hasErrors) {
                alert('Registration form submitted successfully!');
            }
        } else {
            // Handle sign in
            const email = document.getElementById('signin-email').value.trim();
            const password = document.getElementById('signin-password').value.trim();

            if (email && password) {
                alert('Sign in form submitted successfully!');
            } else {
                alert('Please fill in all fields');
            }
        }
    });

    // Add social button event listeners
    document.querySelectorAll('.social-btn').forEach(button => {
        button.addEventListener('click', function () {
            const provider = this.textContent.trim();
            alert(`${provider} login clicked`);
        });
    });
});