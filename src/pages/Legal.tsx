import { FileText, Mail, ShieldCheck } from "lucide-react"
import { Link } from "react-router-dom"

export default function Legal() {
  return (
    <div className="container mx-auto px-4 py-16 max-w-4xl">
      <h1 className="text-4xl font-bold mb-8">Legal & Responsible Disclosure</h1>

      <div className="grid md:grid-cols-2 gap-8 mb-12">
        <div className="bg-card border border-border p-8 rounded-xl">
          <ShieldCheck className="w-10 h-10 text-primary mb-4" />
          <h2 className="text-2xl font-bold mb-4">Authorization Template</h2>
          <p className="text-muted-foreground mb-6">
            Before conducting any security testing, you must obtain written consent. Use our standard authorization
            form.
          </p>
          <a
            href="/AUTHORIZATION_TEMPLATE.md"
            className="inline-flex items-center px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors"
            download
          >
            <FileText className="w-4 h-4 mr-2" />
            Download Template
          </a>
        </div>

        <div className="bg-card border border-border p-8 rounded-xl">
          <Mail className="w-10 h-10 text-primary mb-4" />
          <h2 className="text-2xl font-bold mb-4">Report a Vulnerability</h2>
          <p className="text-muted-foreground mb-6">
            Found a security issue in our toolkit? We appreciate responsible disclosure. Please review our policy before
            submitting.
          </p>
          <Link
            to="/docs#safety"
            className="inline-flex items-center px-4 py-2 bg-secondary text-secondary-foreground rounded-lg hover:bg-secondary/80 transition-colors"
          >
            Read Policy
          </Link>
        </div>
      </div>

      <div className="prose prose-slate dark:prose-invert max-w-none bg-muted/30 p-8 rounded-xl">
        <h3>Responsible Disclosure Policy</h3>
        <p>
          We are committed to ensuring the safety and security of our users. If you believe you have discovered a
          vulnerability in the Windows Penetration Toolkit, please follow these steps:
        </p>
        <ul>
          <li>Do not exploit the vulnerability beyond what is necessary to verify it.</li>
          <li>Do not access or modify user data without permission.</li>
          <li>Submit your report via the contact email provided in the repository.</li>
          <li>Give us reasonable time to remediate the issue before public disclosure.</li>
        </ul>
      </div>
    </div>
  )
}
