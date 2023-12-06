const carousel = document.querySelector('.carousel');
const slides = document.querySelectorAll('.carousel-slide');

let index = 0;

function updateCarousel() {
  const slideWidth = slides[0].clientWidth;
  carousel.style.transform = `translateX(${-index * slideWidth}px)`;
}

function showSlide(n) {
  index = n;
  updateCarousel();
}

function nextSlide() {
  if (index < slides.length - 1) {
    index++;
    updateCarousel();
  }
}

function prevSlide() {
  if (index > 0) {
    index--;
    updateCarousel();
  }
}

// Automatic sliding
setInterval(nextSlide, 5000);

// Initial setup
updateCarousel();


