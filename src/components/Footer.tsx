import { Github, Twitter } from "lucide-react"
import { Link } from "react-router-dom"

export default function Footer() {
  return (
    <footer className="bg-muted/50 border-t border-border mt-auto">
      <div className="container mx-auto px-4 py-12">
        <div className="grid md:grid-cols-4 gap-8 mb-8">
          <div className="col-span-2">
            <h3 className="font-bold text-lg mb-4">Windows Penetration Toolkit</h3>
            <p className="text-muted-foreground max-w-sm">
              An educational platform for safe, simulated security testing training. Built for researchers and students.
            </p>
          </div>

          <div>
            <h4 className="font-semibold mb-4">Resources</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <Link to="/docs" className="hover:text-foreground">
                  Documentation
                </Link>
              </li>
              <li>
                <a href="/downloads/vm-placeholder.zip" className="hover:text-foreground">
                  Download VM
                </a>
              </li>
              <li>
                <Link to="/legal" className="hover:text-foreground">
                  Legal & Safety
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold mb-4">Project</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <a
                  href="https://github.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hover:text-foreground"
                >
                  GitHub
                </a>
              </li>
              <li>
                <a href="/AUTHORIZATION_TEMPLATE.md" className="hover:text-foreground">
                  Authorization Form
                </a>
              </li>
              <li>
                <a href="/RESPONSIBLE_DISCLOSURE.md" className="hover:text-foreground">
                  Security Policy
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-border pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-sm text-muted-foreground">© 2025 Windows Penetration Toolkit. Authorized Use Only.</p>
          <div className="flex gap-4">
            <a href="#" className="text-muted-foreground hover:text-foreground">
              <Github className="w-5 h-5" />
              <span className="sr-only">GitHub</span>
            </a>
            <a href="#" className="text-muted-foreground hover:text-foreground">
              <Twitter className="w-5 h-5" />
              <span className="sr-only">Twitter</span>
            </a>
          </div>
        </div>
      </div>
    </footer>
  )
}
