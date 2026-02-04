// Mobile Menu Toggle - OPTIMIZED: Cache DOM elements
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');
const hamburgerSpans = hamburger ? hamburger.querySelectorAll('span') : [];

if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        
        // Animate hamburger icon - OPTIMIZED: Use cached spans
        if (navMenu.classList.contains('active')) {
            hamburgerSpans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            hamburgerSpans[1].style.opacity = '0';
            hamburgerSpans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
        } else {
            hamburgerSpans[0].style.transform = 'none';
            hamburgerSpans[1].style.opacity = '1';
            hamburgerSpans[2].style.transform = 'none';
        }
    });
}

// Close mobile menu when clicking on a link - OPTIMIZED: Cache nav links
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (navMenu) {
            navMenu.classList.remove('active');
            // Use cached hamburgerSpans
            hamburgerSpans[0].style.transform = 'none';
            hamburgerSpans[1].style.opacity = '1';
            hamburgerSpans[2].style.transform = 'none';
        }
    });
});

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar Background on Scroll - OPTIMIZED: Throttled scroll handler
const navbar = document.querySelector('.navbar');
let scrollTimeout;
let lastScrollTop = 0;

if (navbar) {
    window.addEventListener('scroll', () => {
        // Throttle scroll events to improve performance
        if (scrollTimeout) return;
        
        scrollTimeout = setTimeout(() => {
            const currentScroll = window.pageYOffset;
            
            // Only update if scroll changed significantly (reduce repaints)
            if (Math.abs(currentScroll - lastScrollTop) > 5) {
                if (currentScroll > 50) {
                    navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
                } else {
                    navbar.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.1)';
                }
                lastScrollTop = currentScroll;
            }
            
            scrollTimeout = null;
        }, 50); // Throttle to 50ms
    }, { passive: true }); // Use passive listener for better scrolling performance
}

// Intersection Observer for Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards and feature items
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.about-card, .feature-item, .step');
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s ease';
        observer.observe(el);
    });
});

// Add scroll indicator - OPTIMIZED: Throttled and cached
const scrollIndicator = document.querySelector('.scroll-indicator');
let scrollIndicatorTimeout;

if (scrollIndicator) {
    window.addEventListener('scroll', () => {
        if (scrollIndicatorTimeout) return;
        
        scrollIndicatorTimeout = setTimeout(() => {
            if (window.pageYOffset > 100) {
                scrollIndicator.style.opacity = '0';
            }
            scrollIndicatorTimeout = null;
        }, 100);
    }, { passive: true });
}

// Add particle effect to hero - OPTIMIZED: Reduced frequency and cached hero element
const hero = document.querySelector('.hero');
let particleCount = 0;
const MAX_PARTICLES = 15; // Limit concurrent particles

function createParticle() {
    if (!hero || particleCount >= MAX_PARTICLES) return;
    
    particleCount++;
    const particle = document.createElement('div');
    particle.className = 'particle';
    
    // Generate random values for this specific particle
    const randomX = Math.random() * 100 - 50;
    const randomY = Math.random() * 100 - 50;
    const randomDuration = 3 + Math.random() * 4;
    const startX = Math.random() * 100;
    const startY = Math.random() * 100;
    
    particle.style.cssText = `
        position: absolute;
        width: 4px;
        height: 4px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        pointer-events: none;
        left: ${startX}%;
        top: ${startY}%;
        --random-x: ${randomX}px;
        --random-y: ${randomY}px;
        animation: particle-float ${randomDuration}s ease-in-out forwards;
    `;
    
    hero.appendChild(particle);
    
    setTimeout(() => {
        particle.remove();
        particleCount--;
    }, randomDuration * 1000);
}

// Create particles periodically - OPTIMIZED: Reduced from 300ms to 500ms
if (hero) {
    setInterval(createParticle, 500);
}

// Add CSS for particles - OPTIMIZED: Only add once
if (hero && !document.getElementById('particle-styles')) {
    const style = document.createElement('style');
    style.id = 'particle-styles';
    style.textContent = `
        @keyframes particle-float {
            0% {
                transform: translate(0, 0);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translate(var(--random-x), var(--random-y));
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
}

console.log('✨ Gemini Antigravity Jules CoPilot Lab - Website loaded successfully! (Optimized)');
