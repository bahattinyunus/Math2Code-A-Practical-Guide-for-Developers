import random
import math

def generate_banner(filename="assets/banner.svg"):
    width = 800
    height = 300
    
    # Dark modern background
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#0f172a;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1e293b;stop-opacity:1" />
        </linearGradient>
        <filter id="glow">
            <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="1"/>
        </pattern>
    </defs>
    <rect width="100%" height="100%" fill="url(#grad1)" />
    <rect width="100%" height="100%" fill="url(#grid)" opacity="0.3" />
    '''
    
    # Generate random math symbols floating
    symbols = ['∑', '∫', 'π', '∞', '∆', '∇', '√', '∂', 'λ', 'θ', 'Ω', '{}', '</>', '!=']
    for _ in range(20):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(10, 30)
        opacity = random.random() * 0.3
        char = random.choice(symbols)
        svg_content += f'<text x="{x}" y="{y}" fill="#64748b" font-family="monospace" font-size="{size}" opacity="{opacity}">{char}</text>'
        
    # Draw geometric connecting lines (Constellation effect)
    points = [(random.randint(50, width-50), random.randint(50, height-50)) for _ in range(10)]
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        svg_content += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#3b82f6" stroke-width="1" opacity="0.3" />'
        svg_content += f'<circle cx="{x1}" cy="{y1}" r="3" fill="#3b82f6" opacity="0.5" />'

    # Main Title Text
    svg_content += f'''
    <text x="50%" y="45%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-weight="bold" font-size="50" fill="#f8fafc" filter="url(#glow)">Math2Code</text>
    <text x="50%" y="65%" dominant-baseline="middle" text-anchor="middle" font-family="Courier New, monospace" font-size="20" fill="#94a3b8" letter-spacing="4">THE PRINCIFIA OF CODE</text>
    
    <!-- Code brackets decorative -->
    <text x="10%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="monospace" font-size="100" fill="#334155" opacity="0.2">{{</text>
    <text x="90%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="monospace" font-size="100" fill="#334155" opacity="0.2">}}</text>
    </svg>
    '''
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    generate_banner()
