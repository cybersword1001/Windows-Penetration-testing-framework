import { Search, Server, Key, Network, FileText, Box } from "lucide-react"
import { Link } from "react-router-dom"

const features = [
  {
    icon: Search,
    title: "Automated Recon (Simulated)",
    description: "Visualize network topology and service discovery without sending a single packet.",
  },
  {
    icon: Server,
    title: "SMB Analysis (Simulated)",
    description: "Learn to identify misconfigured file shares and permissions in a safe environment.",
  },
  {
    icon: Key,
    title: "Credential Handling (Simulated)",
    description: "Understand credential dumping techniques and how to defend against them.",
  },
  {
    icon: Network,
    title: "Post-Exploitation Flow (Simulated)",
    description: "Map out lateral movement paths and persistence mechanisms visually.",
  },
  {
    icon: FileText,
    title: "Reporting & Logs",
    description: "Generate comprehensive security assessment reports and audit logs.",
  },
  {
    icon: Box,
    title: "Sandboxed Demos",
    description: "All actions run in a confined, simulated state. Zero risk of damage.",
  },
]

export default function FeatureGrid() {
  return (
    <section className="py-24 bg-muted/50">
      <div className="container mx-auto px-4">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-3xl font-bold mb-4">Comprehensive Security Training</h2>
          <p className="text-muted-foreground text-lg">
            Master the art of Windows penetration testing through our advanced simulation engine. Learn the methodology
            without the liability.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className="bg-background p-6 rounded-xl border border-border hover:border-primary/50 transition-colors shadow-sm hover:shadow-md"
            >
              <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center text-primary mb-4">
                <feature.icon className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
              <p className="text-muted-foreground mb-4">{feature.description}</p>
              <Link to="/docs" className="text-primary font-medium hover:underline inline-flex items-center gap-1">
                Learn more
              </Link>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
