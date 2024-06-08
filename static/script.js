// Search Functionality for Guide Categories
const searchInput = document.getElementById('searchInput'); // Assuming you have a search input field
const categoryGrid = document.getElementById('categoryGrid'); // Assuming you have a grid for your categories

searchInput.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();

    const categoryCards = categoryGrid.querySelectorAll('.category-card');

    categoryCards.forEach(card => {
        const title = card.querySelector('h3').textContent.toLowerCase();

        if (title.includes(searchTerm)) {
            card.style.display = 'block'; // Show if match
        } else {
            card.style.display = 'none'; // Hide if no match
        }
    });
});

// Smooth Scrolling for Navigation Links
const navLinks = document.querySelectorAll('nav a');

navLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default jump

        const targetId = this.getAttribute('href'); // Get the target element ID
        const targetElement = document.querySelector(targetId); // Get the target element

        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth' // Smooth scrolling effect
            });
        }
    });
});

// Example:  Loading Content Dynamically (for Guides)
const guideCards = document.querySelectorAll('.guide-card'); // Assuming you have cards for guides

guideCards.forEach(card => {
    card.addEventListener('click', function() {
        // 1. Get the guide ID or slug from the card's data attribute
        const guideId = this.dataset.guideId; 

        // 2. Fetch the guide content from your Django backend (using AJAX)
        fetch(`/guides/${guideId}/`) 
            .then(response => response.json())
            .then(guideData => {
                // 3. Update the content of a specific section on your page
                const guideContentContainer = document.getElementById('guideContent');
                guideContentContainer.innerHTML = `
                    <h2>${guideData.title}</h2>
                    <p>${guideData.description}</p>
                    ... other content ... 
                `;
            })
            .catch(error => {
                console.error('Error fetching guide data:', error);
            });
    });
});