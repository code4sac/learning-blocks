import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import { AppNextUIProvider } from '@/app/_utilities/providers'
import './globals.css'
import React from 'react'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Learning Blocks',
  description: 'Learning Blocks dashboard.',
}

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
