import math

def generate_banner(filename="assets/banner.svg"):
    width = 800
    height = 300
    
    # Lorenz Attractor Parameters
    sigma = 10
    rho = 28
    beta = 8/3
    dt = 0.01
    x, y, z = 0.1, 0, 0
    points = []
    
    # Generate Lorenz points
    for _ in range(1500):
        dx = sigma * (y - x) * dt
        dy = (x * (rho - z) - y) * dt
        dz = (x * y - beta * z) * dt
        x += dx
        y += dy
        z += dz
        # Project 3D to 2D (simple orthographic projection with offset)
        px = 400 + (x * 15)
        py = 150 + (z * 6) - 150 # Adjusting scale and position
        points.append((px, py))

    # SVG Creation
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="bgGrad" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
            <stop offset="0%" style="stop-color:#1e1b4b;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#020617;stop-opacity:1" />
        </radialGradient>
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#ec4899;stop-opacity:0" />
            <stop offset="50%" style="stop-color:#8b5cf6;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#3b82f6;stop-opacity:0" />
        </linearGradient>
    </defs>
    
    <!-- Deep Space Background -->
    <rect width="100%" height="100%" fill="url(#bgGrad)" />
    
    <!-- Subtle Grid -->
    <defs>
        <pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">
            <path d="M 50 0 L 0 0 0 50" fill="none" stroke="#6366f1" stroke-width="0.5" opacity="0.1"/>
        </pattern>
    </defs>
    <rect width="100%" height="100%" fill="url(#grid)" />

    <!-- Lorenz Attractor Path -->
    <path d="M {points[0][0]} {points[0][1]} '''
    
    for i in range(1, len(points)):
        svg_content += f'L {points[i][0]} {points[i][1]} '
        
    svg_content += f'''" stroke="url(#lineGrad)" stroke-width="2" fill="none" opacity="0.8" filter="url(#glow)" />
    
    <!-- Central Title with "Void" effect -->
    <text x="50%" y="45%" dominant-baseline="middle" text-anchor="middle" font-family="Segoe UI, Helvetica, sans-serif" font-weight="900" font-size="60" fill="white" letter-spacing="2" filter="url(#glow)">Math2Code</text>
    
    <text x="50%" y="65%" dominant-baseline="middle" text-anchor="middle" font-family="Consolas, monospace" font-size="16" fill="#cbd5e1" letter-spacing="6" opacity="0.8">THE SOURCE CODE OF REALITY</text>
    
    <!-- Decorative Elements -->
    <circle cx="400" cy="135" r="120" stroke="white" stroke-width="0.5" fill="none" opacity="0.1" stroke-dasharray="10 5" />
    <circle cx="400" cy="135" r="140" stroke="#8b5cf6" stroke-width="0.5" fill="none" opacity="0.1" stroke-dasharray="20 10" />

    </svg>
    '''
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated Visionary {filename}")

if __name__ == "__main__":
    generate_banner()
