document.getElementById("puppy-btn").addEventListener("click", function() {
    document.getElementById("animal-image").src = "puppy.jpg"; // Update with the correct image path
    document.getElementById("animal-fact").textContent = "Puppies wag their tails when they are happy!";
});

document.getElementById("kitten-btn").addEventListener("click", function() {
    document.getElementById("animal-image").src = "kitten.jpg"; // Update with the correct image path
    document.getElementById("animal-fact").textContent = "Kittens use their whiskers to measure gaps!";
});
