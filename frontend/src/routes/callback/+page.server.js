// import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({url, cookies}) {
	console.log(url.searchParams.get("token"))
	let token = url.searchParams.get("token")
	if (token != null){
		cookies.set("token", token, {
			httpOnly:true
		})
		cookies.set("loggedIn", "true", {
			httpOnly:false
		})
		return {
			status:200
		}
	}
	
	// throw error(404, 'Not found');
}