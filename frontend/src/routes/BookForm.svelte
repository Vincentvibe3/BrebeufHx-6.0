<script lang="ts">
	import { Button, Dropdown, TextInput } from "nota-ui";
  import TagsDisplay from "./TagsDisplay.svelte";

	let age = "";
	let ageValid:boolean;
	let bookValid:boolean;
	let bookLength=""

	let tags = [
		"tag 1", "tag 2", "tag 3","tag 4","tag 5","tag 6","tag 7","tag 8"
		,"tag 9","tag 10","tag 11","tag 12","tag 13", "tag 14", 
		"tag 15", "tag 16", "tag 17", "tag 18", "tag 19", "tag 20", "tag 21", 
		"tag 22", "tag 23", 
	]

	let selectedTags:string[] = []

	let ageRegex = /^[0-9]+$/i

	const verifyAge = () => {
		let matchResult = age.match(ageRegex)
		ageValid = matchResult!=null
	}

	const verifyBookLength = () => {
		let matchResult = bookLength.match(ageRegex)
		bookValid = matchResult!=null
	}

	const submitData = () => {
		console.log({
				age:age,
				pages:bookLength,
				tags:selectedTags,
			})
		// fetch("", 
		// )
	}

</script>
<div class="container">
	<h2>Find books here</h2>
	<div class="step">

		
	</div>
	<p>How old are you?</p>
	<TextInput bind:text={age} on:input={verifyAge} bind:valid={ageValid} placeholder="Age"></TextInput>
	<p>How long do you like your books?</p>
	<TextInput bind:text={bookLength} on:input={verifyBookLength} bind:valid={bookValid} placeholder="Book Length"></TextInput>
	<!-- <Dropdown -->
	<p>What kind of books do you like?</p>
	<TagsDisplay bind:tags={tags} bind:selectedTags={selectedTags} ></TagsDisplay>
	<p>Finish</p>
	<Button on:click={submitData}>Submit</Button>
</div>
<style>

</style>