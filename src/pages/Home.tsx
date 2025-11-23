import Hero from "../components/Hero"
import FeatureGrid from "../components/FeatureGrid"
import DemoPlayer from "../components/DemoPlayer"
import ReduceMotionToggle from "../components/ReduceMotionToggle"

export default function Home() {
  return (
    <div className="flex flex-col">
      <ReduceMotionToggle />
      <Hero />
      <FeatureGrid />
      <DemoPlayer />

      <section className="py-24 bg-muted/30 text-center">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold mb-6">Ready to start learning?</h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto mb-8">
            Download the toolkit and get started with our safe, simulated lab environment. Authorized use only.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <a
              href="/downloads/vm-placeholder.zip"
              className="px-8 py-3 bg-primary text-primary-foreground rounded-lg font-medium hover:bg-primary/90 transition-colors"
            >
              Download VM (Placeholder)
            </a>
            <a
              href="/docs"
              className="px-8 py-3 bg-background border border-input rounded-lg font-medium hover:bg-accent hover:text-accent-foreground transition-colors"
            >
              Read Documentation
            </a>
          </div>
        </div>
      </section>
    </div>
  )
}
