<script>
    import Tasks from './Tasks.svelte';
    import Inputs from "./Inputs.svelte";
    import PromptDisplay from './PromptDisplay.svelte';

    let selectedTask;
    let inputs = [];
    let prompt;

    async function generatePrompt() {
        let rbody = JSON.stringify({
            task_id: selectedTask.id,
            inputs: inputs
        })
        console.log(rbody);

        // call API
        const res = await fetch('/api/generate-prompt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: rbody
        });

        if (res.ok) {
            // get prompt
            const data = await res.json();
            prompt = data.prompt;
        } else {
            console.log("error...")
        }
    }
</script>


<Tasks bind:selected={selectedTask}/>


{#if selectedTask}
    <Inputs bind:selected={selectedTask} on:allinputs={event => inputs = event.detail} />

    <button on:click={generatePrompt}>Generate</button>

    <PromptDisplay {prompt}/>
{/if}