import type { Metadata, Viewport } from 'next'
import { AppNextUIProvider } from '@/utility/providers'
import './globals.css'
import React from 'react'
import { siteConfig } from '@/utility/constants'
import { fontSans } from '@/utility/fonts'
import clsx from 'clsx'

export const metadata: Metadata = {
  title: {
    default: siteConfig.name,
    template: `%s - ${siteConfig.name}`,
  },
  description: siteConfig.description,
}

export const viewport: Viewport = {
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: 'white' },
    { media: '(prefers-color-scheme: dark)', color: 'black' },
  ],
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
    <html suppressHydrationWarning lang="en">
      <head />
      <body
        className={clsx(
          'min-h-screen text-foreground bg-background font-sans antialiased',
          fontSans.variable,
        )}
      >
        <AppNextUIProvider
          themeProps={{ attribute: 'class', defaultTheme: 'light' }}
        >
          {children}
        </AppNextUIProvider>
      </body>
    </html>
  )
}
