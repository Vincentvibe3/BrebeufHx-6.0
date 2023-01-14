<script lang="ts">
	import { Button, Dropdown, TextInput } from "nota-ui";
  import TagsDisplay from "./TagsDisplay.svelte";
  import { env } from "$env/dynamic/public"

	let age = "";
	let ageValid:boolean;
	let bookValid:boolean;
	let bookLength=""
	let datePref=""
	let datePrefOptions:string[] = ['contemporary', 'modern', 'renaissance', 'gothic', 'baroque', 'middle ages', 'antiquity']
	let bookLengthOptions:string[] = ["short", "medium", "long"]
	let tags = [
		"tag 1", "tag 2", "tag 3","tag 4","tag 5","tag 6","tag 7","tag 8"
		,"tag 9","tag 10","tag 11","tag 12","tag 13", "tag 14", 
		"tag 15", "tag 16", "tag 17", "tag 18", "tag 19", "tag 20", "tag 21", 
		"tag 22", "tag 23", 
	]

	let selectedTags:string[] = []

	let ageRegex = /^[0-9]+$/i

	const submitData = async () => {
		// postStatus = "loading"
		let user = {
			date:datePref,
			age:age,
			// tags:tagsToAdd,
			length:bookLength
		}
		let response = await fetch(`${env.PUBLIC_API_SERVER}/addbook`, {
			method:"POST",
			mode:"cors",
			headers:{
				"Content-Type":"application/json"
			},
			// body:JSON.stringify(book)
		})
		// if (response.status!=200){
		// 	postStatus="error"
		// } else {
		// 	postStatus="complete"
		// }
	}

	const verifyAge = () => {
		let matchResult = age.match(ageRegex)
		ageValid = matchResult!=null
	}

	const verifyBookLength = () => {
		let matchResult = bookLength.match(ageRegex)
		bookValid = matchResult!=null
	}


</script>
<div class="container">
	<h2>Find books here</h2>
	<div class="step">

		
	</div>
	<p>How old are you?</p>
	<TextInput bind:text={age} on:input={verifyAge} bind:valid={ageValid} placeholder="Age"></TextInput>
	<p>How long do you like your books?</p>
	<Dropdown bind:optionText={bookLength} bind:options={bookLengthOptions}></Dropdown>
	<p>What era of books do you prefer?</p>
	<Dropdown bind:optionText={datePref} bind:options={datePrefOptions} ></Dropdown>
	<p>What kind of books do you like?</p>
	<TagsDisplay bind:tags={tags} bind:selectedTags={selectedTags} ></TagsDisplay>
	<p>Finish</p>
	<Button on:click={submitData}>Submit</Button>
</div>
<style>

</style>