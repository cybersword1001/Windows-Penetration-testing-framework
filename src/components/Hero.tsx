"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import { ArrowRight, Shield, Terminal } from "lucide-react"
import Lottie from "lottie-react"
import heroAnimation from "../assets/lottie/hero-placeholder.json"
import LegalModal from "./LegalModal"
import { Link } from "react-router-dom"

export default function Hero() {
  const [isModalOpen, setIsModalOpen] = useState(false)

  return (
    <section className="relative pt-20 pb-32 overflow-hidden">
      <div className="container mx-auto px-4">
        <div className="flex flex-col lg:flex-row items-center gap-12">
          <div className="flex-1 space-y-8">
            <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 text-primary text-sm font-medium mb-6">
                <Shield className="w-4 h-4" />
                Safe Simulation Environment
              </div>
              <h1 className="text-4xl md:text-6xl font-bold tracking-tight text-foreground mb-4">
                Windows Penetration Toolkit <br />
                <span className="text-primary">Recon to Post-Exploitation</span>
              </h1>
              <p className="text-xl text-muted-foreground max-w-2xl">
                Automate lab-style recon, exploitation and post-exploitation workflows —<strong> simulated</strong> for
                training and research. No real exploits, just pure education.
              </p>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: 0.2 }}
              className="flex flex-col sm:flex-row gap-4"
            >
              <button
                onClick={() => setIsModalOpen(true)}
                className="inline-flex items-center justify-center px-8 py-4 text-lg font-medium text-primary-foreground bg-primary rounded-lg hover:bg-primary/90 transition-colors gap-2 shadow-lg hover:shadow-primary/25"
              >
                <Terminal className="w-5 h-5" />
                Try Demo (Simulated)
              </button>
              <Link
                to="/docs"
                className="inline-flex items-center justify-center px-8 py-4 text-lg font-medium text-foreground bg-secondary rounded-lg hover:bg-secondary/80 transition-colors gap-2"
              >
                View Docs
                <ArrowRight className="w-5 h-5" />
              </Link>
            </motion.div>
          </div>

          <div className="flex-1 w-full max-w-lg lg:max-w-none">
            <div className="relative aspect-square bg-muted/20 rounded-full blur-3xl absolute -z-10 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%]" />
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, delay: 0.4 }}
              className="relative bg-card border border-border rounded-2xl shadow-2xl overflow-hidden p-6"
            >
              <Lottie animationData={heroAnimation} loop={true} className="w-full h-full" />
            </motion.div>
          </div>
        </div>
      </div>

      <LegalModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
    </section>
  )
}
