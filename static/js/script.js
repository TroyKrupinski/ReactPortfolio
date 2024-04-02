document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent the actual form submission

            const formData = new FormData(contactForm);
            console.log('Form Data Submitted: ', Object.fromEntries(formData.entries()));

            // Here, you would typically send the formData to the server via fetch/AJAX
            // For demonstration, we'll just show an alert
            alert('Thank you for your message!');

            // Reset the form after submission
            contactForm.reset();
        });
    }
});
