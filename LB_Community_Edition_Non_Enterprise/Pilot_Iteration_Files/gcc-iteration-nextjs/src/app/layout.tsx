import './globals.css'
import type { Metadata, Viewport } from 'next'

import React from 'react'
import clsx from 'clsx'

import { AppNextUIProvider } from '@/utility/providers'
import { siteConfig } from '@/utility/constants'
import { fontSans } from '@/utility/fonts'

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

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html suppressHydrationWarning lang="en">
      {/* Suppress hyrdration warning was taken from nextui new project template. */}
      <head />
      <body
        className={clsx(
          'min-h-screen text-foreground bg-background font-sans antialiased',
          fontSans.variable,
        )}
      >
        {/* BUG: Typescript warning the props are missing children. */}
        <AppNextUIProvider
          themeProps={{ attribute: 'class', children, defaultTheme: 'light' }}
        >
          {children}
        </AppNextUIProvider>
      </body>
    </html>
  )
}
