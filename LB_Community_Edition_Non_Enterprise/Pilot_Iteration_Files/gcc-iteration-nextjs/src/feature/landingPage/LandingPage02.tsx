import Image from 'next/image'

export default function LandingPage02() {
  return (
    <div className="relative overflow-hidden">
      <div className="pb-80 pt-16 sm:pb-40 sm:pt-24 lg:pb-48 lg:pt-40">
        <div className="relative mx-auto max-w-7xl px-4 sm:static sm:px-6 lg:px-8">
          <div className="sm:max-w-lg bg-white/50  p-16">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
              Learning Blocks SIS Dashboards
            </h1>
            <p className="mt-4 text-xl text-gray-500">
              Free and open-source dashboard templates for your student
              information system.
            </p>
          </div>
          <div>
            <div className="mt-10">
              {/* Decorative image grid */}
              <div
                aria-hidden="true"
                className="pointer-events-none lg:absolute lg:inset-y-0 lg:mx-auto lg:w-full lg:max-w-7xl"
              >
                <div className="absolute transform sm:left-1/2 sm:top-0 sm:translate-x-8 lg:left-1/2 lg:top-1/2 lg:-translate-y-1/2 lg:translate-x-8">
                  <div className="flex items-center space-x-6 lg:space-x-8">
                    <div className="grid flex-shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                      <div className="h-64 w-44 overflow-hidden rounded-lg sm:opacity-0 lg:opacity-100">
                        <Image
                          alt=""
                          className="h-full w-full object-cover object-center"
                          height={64}
                          src="/a1.jpeg"
                          width={44}
                        />
                      </div>
                      <div className="h-64 w-44 overflow-hidden rounded-lg">
                        <Image
                          alt=""
                          className="h-full w-full object-cover object-center"
                          height={64}
                          src="/a2.jpeg"
                          width={44}
                        />
                      </div>
                    </div>
                    <div className="grid flex-shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                      <div className="h-64 w-44 overflow-hidden rounded-lg">
                        <Image
                          alt=""
                          className="h-full w-full object-cover object-center"
                          height={64}
                          src="/a3.jpeg"
                          width={44}
                        />
                      </div>
                      <div className="h-64 w-44 overflow-hidden rounded-lg">
                        <Image
                          alt=""
                          className="h-full w-full object-cover object-center"
                          height={64}
                          src="/a4.jpeg"
                          width={44}
                        />
                      </div>
                      <div className="h-64 w-44 overflow-hidden rounded-lg">
                        <Image
                          alt=""
                          className="h-full w-full object-cover object-center"
                          height={64}
                          src="/a1.jpeg"
                          width={44}
                        />
                      </div>
                    </div>
                    <div className="grid flex-shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                      <div className="h-64 w-44 overflow-hidden rounded-lg">
                        <Image
                          alt=""
                          className="h-full w-full object-cover object-center"
                          height={64}
                          src="/a1.jpeg"
                          width={44}
                        />
                      </div>
                      <div className="h-64 w-44 overflow-hidden rounded-lg">
                        <Image
                          alt=""
                          className="h-full w-full object-cover object-center"
                          height={64}
                          src="/a1.jpeg"
                          width={44}
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <a
                className="inline-block rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-center font-medium text-white hover:bg-indigo-700"
                href="/dashboard"
              >
                Live Demo
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
