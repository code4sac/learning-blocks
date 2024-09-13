export async function fetchJson(url: string) {
  try {
    let response = await fetch(new URL(url))
    return await response.json()
  } catch (error) {
    return await error
  }
}
