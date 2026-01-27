---
title: Kip Milieu Nonprofit
description: 
date: 2026-01-26 05:00:00 -0500
categories: [post]
tags: [nonprofit]
pin: false
math: true
mermaid: true
pin: false
---
<div style="max-width: 900px; margin: 2rem auto;">
  <iframe
    style="width:100%; aspect-ratio:16/9; border:1px solid #222; background:black;"
    loading="lazy"
    title="Canvas visual experiment"
    srcdoc='
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kip Milieu - 501(c)(3) nonprofit organization</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: #0a0e27;
            color: #ffffff;
            overflow-x: hidden;
        }
        
        /* Gradient backgrounds */
        .gradient-bg {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f172a 100%);
        }
        
        .gradient-glass {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.3) 0%, rgba(51, 65, 85, 0.2) 100%);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .gradient-card {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.4) 0%, rgba(71, 85, 105, 0.3) 100%);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.15);
        }
        
        /* Web3 effects */
        .glow-effect {
            box-shadow: 0 0 40px rgba(59, 130, 246, 0.5);
        }
        
        .neon-border {
            border: 2px solid transparent;
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.3), rgba(30, 41, 59, 0.3)) padding-box,
                        linear-gradient(135deg, #3b82f6, #1e40af) border-box;
        }
        
        /* Floating particles */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }
        
        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(59, 130, 246, 0.6);
            border-radius: 50%;
            animation: float 20s infinite linear;
        }
        
        @keyframes float {
            from {
                transform: translateY(100vh) translateX(0);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            to {
                transform: translateY(-100vh) translateX(100px);
                opacity: 0;
            }
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(30, 41, 59, 0.3);
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #3b82f6, #1e40af);
            border-radius: 4px;
        }
        
        /* Button effects */
        .btn-glow {
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        
        .btn-glow:before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: rgba(59, 130, 246, 0.5);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        .btn-glow:hover:before {
            width: 300px;
            height: 300px;
        }
        
        /* Text gradient */
        .text-gradient {
            background: linear-gradient(135deg, #3b82f6, #60a5fa, #1e40af);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Card hover effects */
        .card-hover {
            transition: all 0.3s ease;
        }
        
        .card-hover:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(59, 130, 246, 0.3);
        }
        
        /* Mobile responsive adjustments */
        @media (max-width: 768px) {
            .gradient-card {
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
            }
        }
    </style>
</head>
<body class="gradient-bg">
    <!-- Particles -->
    <div class="particles" id="particles"></div>
    
    <!-- Navigation -->
    <nav class="gradient-glass sticky top-0 z-50 px-6 py-4">
        <div class="container mx-auto flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-700 rounded-lg flex items-center justify-center">
                    <span class="text-white font-bold text-lg">KM</span>
                </div>
                <span class="text-xl font-semibold">Kip Milieu</span>
            </div>
            <div class="hidden md:flex space-x-8">
                <a href="#mission" class="hover:text-blue-400 transition">Mission</a>
                <a href="#tiers" class="hover:text-blue-400 transition">Support</a>
                <a href="#purposes" class="hover:text-blue-400 transition">Purposes</a>
                <a href="#goals" class="hover:text-blue-400 transition">Goals</a>
                <a href="#faq" class="hover:text-blue-400 transition">FAQ</a>
            </div>
            <button class="md:hidden" onclick="toggleMobileMenu()">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                </svg>
            </button>
        </div>
        <!-- Mobile menu -->
        <div id="mobileMenu" class="hidden md:hidden mt-4 space-y-2">
            <a href="#mission" class="block py-2 hover:text-blue-400 transition">Mission</a>
            <a href="#tiers" class="block py-2 hover:text-blue-400 transition">Support</a>
            <a href="#purposes" class="block py-2 hover:text-blue-400 transition">Purposes</a>
            <a href="#goals" class="block py-2 hover:text-blue-400 transition">Goals</a>
            <a href="#faq" class="block py-2 hover:text-blue-400 transition">FAQ</a>
        </div>
    </nav>
    
    <!-- Hero Section -->
    <section class="min-h-screen flex items-center justify-center px-6 relative z-10">
        <div class="text-center max-w-4xl mx-auto" data-aos="fade-up">
            <h1 class="text-5xl md:text-7xl font-bold mb-6">
                <span class="text-gradient">Kip Milieu</span>
            </h1>
            <p class="text-2xl md:text-3xl text-blue-300 mb-4">501(c)(3) nonprofit organization</p>
            <p class="text-lg md:text-xl text-gray-300 mb-8 leading-relaxed">
                Inspiring people to explore new ideas, embrace diverse perspectives, and venture beyond their comfort zone. 
                Creating a community of growth, curiosity, and transformation.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://collect.crowded.me/collection/e82547c3-b8c5-4d84-99a7-6627736dafda">
                <button class="neon-border px-8 py-4 rounded-lg font-semibold hover:scale-105 transition">    
                    Donate
                </button>
                </a>
                <a href="#purposes">
                <button class="btn-glow gradient-glass px-8 py-4 rounded-lg font-semibold hover:scale-105 transition">
                    Learn More
                </button>
                </a>
            </div>
        </div>
    </section>
    
    <!-- Mission Section -->
    <section id="mission" class="py-20 px-6 relative z-10">
        <div class="container mx-auto">
            <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-gradient" data-aos="fade-up">
                Our Mission
            </h2>
            <div class="gradient-glass rounded-2xl p-8 md:p-12 max-w-4xl mx-auto" data-aos="fade-up" data-aos-delay="200">
                <p class="text-lg md:text-xl leading-relaxed text-gray-200">
                    The missions of Kip Milieu is to inspire people to explore new ideas, embrace every perspective, 
                    and go well beyond their comfort zone. We strive to create a community of growth, curiosity, 
                    and transformation by embracing new experiences.
                </p>
            </div>
        </div>
    </section>
    
    <!-- Support Tiers -->
    <section id="tiers" class="py-20 px-6 relative z-10">
        <div class="container mx-auto">
            <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-gradient" data-aos="fade-up">
                Support Our Mission
            </h2>
            <p class="text-center text-gray-300 mb-12 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="100">
                Support us monthly in achieving the mission and purpose of our organization
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Standard Tier -->
                <div class="gradient-card rounded-xl p-6 card-hover" data-aos="fade-up" data-aos-delay="200">
                    <h3 class="text-xl font-semibold mb-2">Standard</h3>
                    <div class="text-3xl font-bold text-blue-400 mb-4">$1<span class="text-lg">/mo</span></div>
                    <p class="text-gray-300 mb-6">Every dollar helps in achieving our mission</p>
                    <a href="https://collect.crowded.me/collection/e82547c3-b8c5-4d84-99a7-6627736dafda">
                    <button class="w-full btn-glow gradient-glass py-3 rounded-lg font-medium hover:scale-105 transition">
                        Select Tier
                    </button>
                    </a>
                </div>
                
                <!-- Gold Tier -->
                <div class="gradient-card rounded-xl p-6 card-hover border-2 border-blue-500/50" data-aos="fade-up" data-aos-delay="300">
                    <h3 class="text-xl font-semibold mb-2">Gold</h3>
                    <div class="text-3xl font-bold text-blue-400 mb-4">$10<span class="text-lg">/mo</span></div>
                    <p class="text-gray-300 mb-6">Help to keep our operations running</p>
                    <a href="https://collect.crowded.me/collection/e82547c3-b8c5-4d84-99a7-6627736dafda">
                    <button class="w-full btn-glow gradient-glass py-3 rounded-lg font-medium hover:scale-105 transition">
                        Select Tier
                    </button>
                    </a>
                </div>
                
                <!-- Diamond Tier -->
                <div class="gradient-card rounded-xl p-6 card-hover border-2 border-purple-500/50" data-aos="fade-up" data-aos-delay="400">
                    <h3 class="text-xl font-semibold mb-2">Diamond</h3>
                    <div class="text-3xl font-bold text-purple-400 mb-4">$50<span class="text-lg">/mo</span></div>
                    <p class="text-gray-300 mb-6">Help to keep operations running and a little more</p>
                    <a href="https://collect.crowded.me/collection/e82547c3-b8c5-4d84-99a7-6627736dafda">
                    <button class="w-full btn-glow gradient-glass py-3 rounded-lg font-medium hover:scale-105 transition">
                        Select Tier
                    </button>
                    </a>
                </div>
                
                <!-- Platinum Tier -->
                <div class="gradient-card rounded-xl p-6 card-hover border-2 border-yellow-500/50" data-aos="fade-up" data-aos-delay="500">
                    <h3 class="text-xl font-semibold mb-2">Platinum</h3>
                    <div class="text-3xl font-bold text-yellow-400 mb-4">$100<span class="text-lg">+/mo</span></div>
                    <p class="text-gray-300 mb-6">Help to become an impactful member of our community</p>
                    <a href="https://collect.crowded.me/collection/e82547c3-b8c5-4d84-99a7-6627736dafda">
                    <button class="w-full btn-glow gradient-glass py-3 rounded-lg font-medium hover:scale-105 transition">
                        Select Tier
                    </button>
                    </a>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Purposes Section -->
    <section id="purposes" class="py-20 px-6 relative z-10">
        <div class="container mx-auto">
            <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-gradient" data-aos="fade-up">
                Our Purposes
            </h2>
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <!-- Educational -->
                <div class="gradient-card rounded-2xl p-8 card-hover" data-aos="fade-up" data-aos-delay="200">
                    <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-700 rounded-xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                        </svg>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4">Educational</h3>
                    <p class="text-gray-300 mb-6">
                        Our organization is committed to fostering knowledge and personal growth through accessible 
                        learning opportunities and innovative educational programs.
                    </p>
                    <ul class="space-y-3 text-gray-300">
                        <li class="flex items-start">
                            <span class="text-blue-400 mr-2">•</span>
                            Develop programs for lifelong learning and critical thinking
                        </li>
                        <li class="flex items-start">
                            <span class="text-blue-400 mr-2">•</span>
                            Host workshops across diverse fields
                        </li>
                        <li class="flex items-start">
                            <span class="text-blue-400 mr-2">•</span>
                            Provide resources and mentorship
                        </li>
                    </ul>
                </div>
                
                <!-- Charitable -->
                <div class="gradient-card rounded-2xl p-8 card-hover" data-aos="fade-up" data-aos-delay="300">
                    <div class="w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-700 rounded-xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                        </svg>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4">Charitable</h3>
                    <p class="text-gray-300 mb-6">
                        Creating a more equitable world by supporting communities in need through 
                        collaboration and advocacy for meaningful impact.
                    </p>
                    <ul class="space-y-3 text-gray-300">
                        <li class="flex items-start">
                            <span class="text-purple-400 mr-2">•</span>
                            Collaborate with nonprofits to amplify impact
                        </li>
                        <li class="flex items-start">
                            <span class="text-purple-400 mr-2">•</span>
                            Advocate for equity and inclusion
                        </li>
                        <li class="flex items-start">
                            <span class="text-purple-400 mr-2">•</span>
                            Support underprivileged communities
                        </li>
                    </ul>
                </div>
                
                <!-- Scientific -->
                <div class="gradient-card rounded-2xl p-8 card-hover" data-aos="fade-up" data-aos-delay="400">
                    <div class="w-16 h-16 bg-gradient-to-br from-green-500 to-green-700 rounded-xl flex items-center justify-center mb-6">
                        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
                        </svg>
                    </div>
                    <h3 class="text-2xl font-semibold mb-4">Scientific</h3>
                    <p class="text-gray-300 mb-6">
                        Advancing scientific understanding through research and discovery, working 
                        responsibly to solve real-world challenges.
                    </p>
                    <ul class="space-y-3 text-gray-300">
                        <li class="flex items-start">
                            <span class="text-green-400 mr-2">•</span>
                            Provide research grants for innovation
                        </li>
                        <li class="flex items-start">
                            <span class="text-green-400 mr-2">•</span>
                            Share findings openly for collaboration
                        </li>
                        <li class="flex items-start">
                            <span class="text-green-400 mr-2">•</span>
                            Apply science to solve real-world problems
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Goals Section -->
    <section id="goals" class="py-20 px-6 relative z-10">
        <div class="container mx-auto">
            <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-gradient" data-aos="fade-up">
                Our Goals
            </h2>
            <p class="text-center text-gray-300 mb-12 max-w-2xl mx-auto" data-aos="fade-up" data-aos-delay="100">
                We strive to make an impact on as many people as possible
            </p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="text-center" data-aos="fade-up" data-aos-delay="200">
                    <div class="text-5xl md:text-6xl font-bold text-blue-400 mb-4">
                        <span class="counter" data-target="10000">0</span>+
                    </div>
                    <h3 class="text-xl font-semibold text-gray-200">New Perspectives</h3>
                </div>
                <div class="text-center" data-aos="fade-up" data-aos-delay="300">
                    <div class="text-5xl md:text-6xl font-bold text-purple-400 mb-4">
                        <span class="counter" data-target="1000">0</span>+
                    </div>
                    <h3 class="text-xl font-semibold text-gray-200">People Helped</h3>
                </div>
                <div class="text-center" data-aos="fade-up" data-aos-delay="400">
                    <div class="text-5xl md:text-6xl font-bold text-green-400 mb-4">
                        <span class="counter" data-target="100">0</span>+
                    </div>
                    <h3 class="text-xl font-semibold text-gray-200">New Discoveries</h3>
                </div>
            </div>
        </div>
    </section>
    
    <!-- FAQ Section -->
    <section id="faq" class="py-20 px-6 relative z-10">
        <div class="container mx-auto max-w-4xl">
            <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-gradient" data-aos="fade-up">
                Frequently Asked Questions
            </h2>
            <div class="space-y-6">
                <div class="gradient-card rounded-xl overflow-hidden" data-aos="fade-up" data-aos-delay="100">
                    <button class="w-full p-6 text-left flex justify-between items-center" onclick="toggleFAQ(1)">
                        <h3 class="text-lg font-semibold">What does Kip Milieu mean?</h3>
                        <svg class="w-6 h-6 transform transition-transform" id="faq-icon-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </button>
                    <div class="px-6 pb-6 hidden" id="faq-content-1">
                        <p class="text-gray-300">
                            Kip Milieu is a conjunction of an acronym and French word. KIP stands for Knowledge-is-Power 
                            and symbolizes that the only limitation to achieving something in the world is what you know. 
                            Contrasting with the French word 'Milieu' (a person's social environment), there is an understanding 
                            that "it's not what you know, it's who you know" that holds true when trying to put learning into 
                            action and collaboration.
                        </p>
                    </div>
                </div>
                
                <div class="gradient-card rounded-xl overflow-hidden" data-aos="fade-up" data-aos-delay="200">
                    <button class="w-full p-6 text-left flex justify-between items-center" onclick="toggleFAQ(2)">
                        <h3 class="text-lg font-semibold">Why was Kip Milieu formed?</h3>
                        <svg class="w-6 h-6 transform transition-transform" id="faq-icon-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </button>
                    <div class="px-6 pb-6 hidden" id="faq-content-2">
                        <p class="text-gray-300">
                            We were formed out of a desire to help other people while at the same time understanding 
                            that interdisciplinary learning is as important as an expertise in a specific subject area.
                        </p>
                    </div>
                </div>
                
                <div class="gradient-card rounded-xl overflow-hidden" data-aos="fade-up" data-aos-delay="300">
                    <button class="w-full p-6 text-left flex justify-between items-center" onclick="toggleFAQ(3)">
                        <h3 class="text-lg font-semibold">If I want to get involved, who can I contact?</h3>
                        <svg class="w-6 h-6 transform transition-transform" id="faq-icon-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </button>
                    <div class="px-6 pb-6 hidden" id="faq-content-3">
                        <p class="text-gray-300">
                            Our main point of contact is currently Erik Makela. You can reach out to him on any of his social media platforms.
                        </p>
                    </div>
                </div>
                
                <div class="gradient-card rounded-xl overflow-hidden" data-aos="fade-up" data-aos-delay="400">
                    <button class="w-full p-6 text-left flex justify-between items-center" onclick="toggleFAQ(4)">
                        <h3 class="text-lg font-semibold">What exactly do you mean by explore new experiences?</h3>
                        <svg class="w-6 h-6 transform transition-transform" id="faq-icon-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                        </svg>
                    </button>
                    <div class="px-6 pb-6 hidden" id="faq-content-4">
                        <p class="text-gray-300">
                            As Paul Graham explains: "The clash of domains is a particularly fruitful source of ideas. 
                            If you know a lot about programming and you start learning about some other field, you'll 
                            probably see problems that software could solve. In fact, you're doubly likely to find good 
                            problems in another domain: (a) the inhabitants of that domain are not as likely as software 
                            people to have already solved their problems with software, and (b) since you come into the 
                            new domain totally ignorant, you don't even know what the status quo is to take it for granted."
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Footer -->
    <footer class="gradient-glass py-12 px-6 relative z-10">
        <div class="container mx-auto text-center">
            <div class="flex justify-center items-center space-x-2 mb-6">
                <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-700 rounded-lg flex items-center justify-center">
                    <span class="text-white font-bold text-lg">KM</span>
                </div>
                <span class="text-xl font-semibold">Kip Milieu</span>
            </div>
            <p class="text-gray-400 mb-6">501(c)(3) Nonprofit Organization</p>
            <p class="text-gray-500 text-sm">Kip Milieu. All rights reserved.</p>
        </div>
    </footer>
    
    <script>
        // Initialize particles
        function createParticles() {
            const particlesContainer = document.getElementById('particles');
            const particleCount = 50;
            
            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 20 + 's';
                particle.style.animationDuration = (Math.random() * 20 + 10) + 's';
                particlesContainer.appendChild(particle);
            }
        }
        
        // Toggle mobile menu
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            menu.classList.toggle('hidden');
        }
        
        // Toggle FAQ items
        function toggleFAQ(id) {
            const content = document.getElementById(`faq-content-${id}`);
            const icon = document.getElementById(`faq-icon-${id}`);
            
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate-180');
        }
        
        // Counter animation
        function animateCounters() {
            const counters = document.querySelectorAll('.counter');
            
            counters.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-target'));
                const increment = target / 100;
                let current = 0;
                
                const updateCounter = () => {
                    current += increment;
                    if (current < target) {
                        counter.textContent = Math.ceil(current).toLocaleString();
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target.toLocaleString();
                    }
                };
                
                updateCounter();
            });
        }
        
        // Initialize AOS
        AOS.init({
            duration: 1000,
            once: true,
            offset: 100
        });
        
        // Start animations when page loads
        document.addEventListener('DOMContentLoaded', function() {
            createParticles();
            
            // Start counter animation when goals section is in view
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        animateCounters();
                        observer.disconnect();
                    }
                });
            });
            
            const goalsSection = document.getElementById('goals');
            if (goalsSection) {
                observer.observe(goalsSection);
            }
        });
        
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    // Close mobile menu if open
                    const mobileMenu = document.getElementById('mobileMenu');
                    if (!mobileMenu.classList.contains('hidden')) {
                        mobileMenu.classList.add('hidden');
                    }
                }
            });
        });
    </script>
</body>
</html>
'>
  </iframe>
</div>

