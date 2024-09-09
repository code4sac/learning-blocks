import type { Metadata, Viewport } from 'next'
import { AppNextUIProvider } from '@/providers'
import './globals.css'
import React from 'react'
import { siteConfig } from '@/constants'

export const metadata: Metadata = {
  title: {
    default: siteConfig.name,
    template: `%s - ${siteConfig.name}`,
  },
  description: siteConfig.description,
}

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "white" },
    { media: "(prefers-color-scheme: dark)", color: "black" },
  ],
};

/**
 * Root layout component.
 *
 * @param children - The children components to be rendered.
 * @returns The rendered RootLayout component.
 */
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className={`${inter.className} text-foreground bg-background`}>
        <AppNextUIProvider>{children}</AppNextUIProvider>
      </body>
    </html>
  )
}
