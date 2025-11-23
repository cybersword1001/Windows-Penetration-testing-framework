"use client"

import { useState, useEffect } from "react"
import { MousePointer2, Zap } from "lucide-react"

export default function ReduceMotionToggle() {
  const [reduceMotion, setReduceMotion] = useState(false)

  useEffect(() => {
    const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)")
    setReduceMotion(mediaQuery.matches)

    const handleChange = () => setReduceMotion(mediaQuery.matches)
    mediaQuery.addEventListener("change", handleChange)
    return () => mediaQuery.removeEventListener("change", handleChange)
  }, [])

  return (
    <button
      onClick={() => setReduceMotion(!reduceMotion)}
      className="fixed bottom-4 right-4 z-50 p-2 bg-secondary/80 backdrop-blur rounded-full shadow-lg hover:bg-secondary transition-colors"
      title={reduceMotion ? "Enable animations" : "Reduce motion"}
      aria-pressed={reduceMotion}
    >
      {reduceMotion ? <MousePointer2 className="w-5 h-5" /> : <Zap className="w-5 h-5" />}
      <span className="sr-only">Toggle reduced motion</span>
    </button>
  )
}
