// @ts-nocheck
/** @type {import('./$types').PageLoad} */
// @ts-ignore
export async function load({ params }) {
	return {
		bookId:params.id,
	}
  }