"use client"

import { useState } from "react"
import { Play, Terminal } from "lucide-react"

export default function DemoPlayer() {
  const [isPlaying, setIsPlaying] = useState(false)

  return (
    <section className="py-24 container mx-auto px-4">
      <div className="grid lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <div className="bg-black rounded-xl overflow-hidden border border-zinc-800 shadow-2xl aspect-video relative group">
            {isPlaying ? (
              <video src="/media/demo-screencast.mp4" autoPlay controls className="w-full h-full object-cover" />
            ) : (
              <div className="absolute inset-0 flex flex-col items-center justify-center bg-zinc-950">
                <Terminal className="w-16 h-16 text-zinc-700 mb-4" />
                <button
                  onClick={() => setIsPlaying(true)}
                  className="bg-primary text-primary-foreground rounded-full p-4 hover:scale-110 transition-transform shadow-lg"
                >
                  <Play className="w-8 h-8 fill-current ml-1" />
                </button>
                <p className="text-zinc-500 mt-4">Click to run simulated attack flow</p>
              </div>
            )}
          </div>
        </div>

        <div className="space-y-6">
          <h3 className="text-2xl font-bold">Simulation Flow</h3>
          <div className="space-y-4">
            {[
              {
                step: "01",
                title: "Reconnaissance",
                status: "Completed",
                desc: "Simulated port scan & service enumeration",
              },
              {
                step: "02",
                title: "Vulnerability Check",
                status: "Simulated",
                desc: "Detecting SMBv1 configurations (Mocked)",
              },
              { step: "03", title: "Exploitation", status: "Simulated", desc: "Safe execution of exploit chain" },
              { step: "04", title: "Post-Exploitation", status: "Pending", desc: "Lateral movement visualization" },
            ].map((item, i) => (
              <div key={i} className="flex gap-4 p-4 rounded-lg bg-muted/30 border border-border">
                <div className="text-2xl font-bold text-muted-foreground/30">{item.step}</div>
                <div>
                  <div className="flex justify-between items-center mb-1">
                    <h4 className="font-semibold">{item.title}</h4>
                    <span className="text-xs bg-primary/10 text-primary px-2 py-1 rounded-full">{item.status}</span>
                  </div>
                  <p className="text-sm text-muted-foreground">{item.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
