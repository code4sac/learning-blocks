'use client'; // Ensure this directive is present if you use client-side components

import {ThemeProvider} from 'react-bootstrap'; // Import ThemeProvider from react-bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS globally
import type {AppProps} from 'next/app'; // Import AppProps type from Next.js

function MyApp({Component, pageProps}: AppProps) {
  return (
    <ThemeProvider>
      <Component {...pageProps} />
    </ThemeProvider>
  );
}

export default MyApp;
