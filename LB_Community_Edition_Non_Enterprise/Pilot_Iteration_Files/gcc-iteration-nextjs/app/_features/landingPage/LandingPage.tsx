import { Link } from "@nextui-org/react";

export default function LandingPage() {
  return (
    <div>
      <div className="container mx-auto max-w-prose">
        <h1 className="font">Learning Blocks Landing Page</h1>
        <ul className="list-[upper-roman]">
          <li>
            <Link href="/dashboard">Dashboard</Link>
          </li>
        </ul>
      </div>
    </div>
  );
}
