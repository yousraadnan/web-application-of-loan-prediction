// script.js

// Function to handle navigation
document.addEventListener('DOMContentLoaded', () => {
    const homeButton = document.querySelector('.btn-primary');
    const applyButton = document.querySelector('.btn-secondary');

    homeButton.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default anchor behavior
        alert('Navigating to Home'); // Replace with actual navigation logic
    });

    applyButton.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default anchor behavior
        alert('Navigating to Apply for Loan'); // Replace with actual navigation logic
    });
});



