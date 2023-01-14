// @ts-nocheck
/** @type {import('./$types').PageLoad} */
// @ts-ignore
export async function load({ params }) {

	let response = await fetch(`${env.PUBLIC_API_SERVER}book/${params.id}`)
	if (response.status==200){
		return {
			bookId:params.id,
			book:response.json
		}
	}

	throw error(404, 'Not found');
  }