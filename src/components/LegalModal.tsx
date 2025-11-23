"use client"

import { X, Download, ShieldAlert } from "lucide-react"
import { motion, AnimatePresence } from "framer-motion"

interface LegalModalProps {
  isOpen: boolean
  onClose: () => void
}

export default function LegalModal({ isOpen, onClose }: LegalModalProps) {
  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.95 }}
            className="bg-background w-full max-w-2xl rounded-lg shadow-2xl border border-border overflow-hidden"
          >
            <div className="p-6 border-b border-border flex justify-between items-center bg-muted/30">
              <div className="flex items-center gap-2 text-destructive">
                <ShieldAlert className="w-6 h-6" />
                <h2 className="text-xl font-bold">Authorized Use Only</h2>
              </div>
              <button onClick={onClose} className="text-muted-foreground hover:text-foreground">
                <X className="w-6 h-6" />
              </button>
            </div>

            <div className="p-6 space-y-4 overflow-y-auto max-h-[60vh]">
              <div className="bg-yellow-500/10 border border-yellow-500/20 p-4 rounded-md text-sm text-yellow-600 dark:text-yellow-400">
                <strong>Legal Warning:</strong> This tool is for educational and authorized testing purposes only. You
                must have explicit written permission from the system owner before using any penetration testing tools.
              </div>

              <h3 className="font-semibold text-lg">Authorization Required</h3>
              <p className="text-muted-foreground">
                By downloading or using the Windows Penetration Toolkit, you verify that you understand local and
                international laws regarding cybersecurity testing.
              </p>

              <div className="space-y-2">
                <h4 className="font-medium">You agree to:</h4>
                <ul className="list-disc pl-5 space-y-1 text-muted-foreground">
                  <li>Only test systems you own or have written permission to test.</li>
                  <li>Follow responsible disclosure guidelines for any findings.</li>
                  <li>Not use this software for malicious purposes.</li>
                </ul>
              </div>
            </div>

            <div className="p-6 border-t border-border bg-muted/30 flex justify-between items-center">
              <a
                href="/AUTHORIZATION_TEMPLATE.md"
                download
                className="flex items-center gap-2 text-primary hover:underline"
              >
                <Download className="w-4 h-4" />
                Download Authorization Template
              </a>
              <div className="flex gap-3">
                <button
                  onClick={onClose}
                  className="px-4 py-2 text-muted-foreground hover:text-foreground transition-colors"
                >
                  Cancel
                </button>
                <button
                  onClick={onClose}
                  className="px-4 py-2 bg-primary text-primary-foreground rounded-md hover:bg-primary/90 transition-colors font-medium"
                >
                  I Understand & Agree
                </button>
              </div>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  )
}
