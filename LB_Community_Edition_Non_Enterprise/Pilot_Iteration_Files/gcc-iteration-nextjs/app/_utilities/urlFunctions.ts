export function getRedirectUrl(location: Location) {
  const searchParams = new URLSearchParams(location.search);
  if (searchParams.size > 0) {
    return decodeURIComponent(searchParams.get("redirect")!);
  } else {
    return "/";
  }
}
