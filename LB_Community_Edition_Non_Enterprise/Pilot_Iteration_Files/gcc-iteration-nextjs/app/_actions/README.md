# Actions Pattern in Next.js

The actions pattern in Next.js involves several key steps to handle data fetching, form submissions, and state
management. Below is a detailed explanation of each step:

## 1. Define API Routes

Create API routes in the `pages/api` directory to handle server-side logic.

Example:

```tsx
// pages/api/data.js
export default function handler(req, res) {
  if (req.method === 'GET') {
    res.status(200).json({ data: 'Sample Data' });
  }
}
```

## 2. Fetch Data

Use getServerSideProps, getStaticProps, or getInitialProps to fetch data on the server-side.

Example:

```tsx
// pages/index.js
export async function getServerSideProps() {
  const res = await fetch('http://localhost:3000/api/data');
  const data = await res.json();
  return { props: { data } };
}
```

## 3. Client-Side Fetching

Use useEffect or SWR (stale-while-revalidate) for client-side data fetching.

Example:

```tsx
import useSWR from 'swr';

const fetcher = (url) => fetch(url).then((res) => res.json());

function Component() {
  const { data, error } = useSWR('/api/data', fetcher);

  if (error) return <div>Failed to load</div>;
  if (!data) return <div>Loading...</div>;

  return <div>{data.data}</div>;
}
```

## 4. Handle Forms

Use form handlers to manage form submissions and interact with API routes.

Example:

```tsx
// pages/index.js
import { useState } from 'react';

export default function Home({ data }) {
  const [formData, setFormData] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ formData }),
    });
    const result = await res.json();
    console.log(result);
  };

  return (
    <div>
      <h1>{data.data}</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={formData}
          onChange={(e) => setFormData(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
```

## 5. State Management

Use React's useState and useReducer for local state, or libraries like Redux for global state management.
Create API routes in the `pages/api` directory to handle server-side logic.

Example:

```tsx
/import { useReducer } from 'react';

const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <>
      Count: {state.count}
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </>
  );
}
```

## 6. Routing

Use Next.js's built-in routing for navigation between pages.

Example:

```tsx
import Link from 'next/link';

function HomePage() {
  return (
    <div>
      <h1>Home Page</h1>
      <Link href="/about">
        <a>About Page</a>
      </Link>
    </div>
  );
}

export default HomePage;
```
