import { Link } from "react-router-dom"
import { ArrowLeft, Shield } from "lucide-react"

export default function Docs() {
  return (
    <div className="container mx-auto px-4 py-12">
      <Link to="/" className="inline-flex items-center text-muted-foreground hover:text-foreground mb-8">
        <ArrowLeft className="w-4 h-4 mr-2" />
        Back to Home
      </Link>

      <div className="grid lg:grid-cols-[240px_1fr] gap-12">
        <aside className="space-y-6">
          <div className="font-bold text-lg mb-4">Documentation</div>
          <nav className="space-y-2 text-sm text-muted-foreground">
            <a href="#intro" className="block hover:text-foreground transition-colors">
              Introduction
            </a>
            <a href="#quickstart" className="block hover:text-foreground transition-colors">
              Quick Start
            </a>
            <a href="#architecture" className="block hover:text-foreground transition-colors">
              Architecture
            </a>
            <a href="#safety" className="block hover:text-foreground transition-colors">
              Safety Guidelines
            </a>
          </nav>
        </aside>

        <div className="prose prose-slate dark:prose-invert max-w-none">
          <h1 id="intro">Documentation</h1>
          <p className="lead">
            The Windows Penetration Toolkit is a comprehensive learning platform designed to teach security
            professionals about Windows environment vulnerabilities in a safe, simulated manner.
          </p>

          <div className="bg-yellow-500/10 border border-yellow-500/20 p-6 rounded-lg my-8">
            <h3 className="text-yellow-600 dark:text-yellow-400 mt-0 flex items-center gap-2">
              <Shield className="w-5 h-5" />
              Safety Notice
            </h3>
            <p className="mb-0 text-sm">
              This tool simulates attacks using mocked data and recorded interactions. It does not contain actual
              exploit code or malicious payloads.
            </p>
          </div>

          <h2 id="quickstart">Quick Start</h2>
          <p>Clone the repository and start the simulation environment:</p>
          <pre className="bg-muted p-4 rounded-lg overflow-x-auto">
            <code>
              git clone https://github.com/yourusername/windows-penetration-toolkit.git{"\n"}
              cd windows-penetration-toolkit{"\n"}
              npm install{"\n"}
              npm run dev
            </code>
          </pre>

          <h2 id="architecture">Architecture</h2>
          <div className="my-8 p-8 bg-muted rounded-lg flex justify-center">
            {/* Simple SVG Architecture Diagram */}
            <svg width="400" height="200" viewBox="0 0 400 200" className="w-full max-w-md">
              <g fill="none" stroke="currentColor" strokeWidth="2">
                <rect x="20" y="80" width="80" height="40" rx="4" />
                <text x="60" y="105" textAnchor="middle" fill="currentColor" stroke="none" fontSize="12">
                  CLI Core
                </text>

                <path d="M100 100 h 60" markerEnd="url(#arrow)" />

                <rect x="160" y="80" width="80" height="40" rx="4" />
                <text x="200" y="105" textAnchor="middle" fill="currentColor" stroke="none" fontSize="12">
                  Web UI
                </text>

                <path d="M240 100 h 60" markerEnd="url(#arrow)" />

                <rect x="300" y="80" width="80" height="40" rx="4" />
                <text x="340" y="105" textAnchor="middle" fill="currentColor" stroke="none" fontSize="12">
                  Simulation
                </text>
              </g>
              <defs>
                <marker
                  id="arrow"
                  markerWidth="10"
                  markerHeight="10"
                  refX="9"
                  refY="3"
                  orient="auto"
                  markerUnits="strokeWidth"
                >
                  <path d="M0,0 L0,6 L9,3 z" fill="currentColor" />
                </marker>
              </defs>
            </svg>
          </div>

          <h2 id="safety">Safety & Legal</h2>
          <p>
            This tool is strictly for educational purposes. It does not generate malicious network traffic. Always
            obtain written permission before testing any system.
          </p>
        </div>
      </div>
    </div>
  )
}
