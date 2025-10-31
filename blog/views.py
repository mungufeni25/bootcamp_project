from django.shortcuts import render
import random

blogs = [
    "Every designer knows you need to showcase your best work. But in today's crowded market, simply showing the final logo or website isn't enough to secure a high-value client or a dream job. You need to prove you’re more than just a creative hand—you need to prove you're a strategic partner and a business problem-solver."
    "In the competitive world of design, standing out requires more than just talent. A well-crafted portfolio that tells a story and highlights your unique approach can make all the difference. It's not just about showing what you've done; it's about demonstrating how you think and solve problems.",
    "A compelling design portfolio is your ticket to attracting high-value clients and landing your dream job. It's not just a collection of your best work; it's a narrative that showcases your strategic thinking, creativity, and ability to solve complex business challenges through design.",
    "To create a portfolio that truly resonates, focus on storytelling. Each project should highlight the challenges faced, the solutions you devised, and the impact of your work. This approach not only showcases your skills but also positions you as a thoughtful and strategic designer."
]

images = [
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80",
    "https://images.unsplash.com/photo-1467003909585-2f8a72700288?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80",
    "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80"
]

def blog(request):
    random_blog = random.choice(blogs)
    random_image = random.choice(images)
    
    context = {
        'blog': random_blog,
        'image': random_image
    }
    return render(request, 'blog/blog.html', context)

def show_all(request):
    context = {
        'blogs': blogs,
        'images': images
    }
    return render(request, 'blog/show_all.html', context)

def about(request):
    return render(request, 'blog/about.html')