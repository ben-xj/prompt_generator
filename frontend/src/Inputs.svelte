<!-- Inputs.svelte -->

<script>
    import {createEventDispatcher} from 'svelte';

    const dispatch = createEventDispatcher();

    export let selected;

    let inputs = [];


    $:    if (selected) {
        const previousInputs = inputs;
        inputs = new Array(selected.num_inputs).fill('');

        for (let i = 0; i < inputs.length; i++) {
            inputs[i] = previousInputs[i] || '';
        }
    }


    function onInput(e) {
        inputs[e.target.dataset.index] = e.target.value;
        dispatch('allinputs', inputs);
    }
</script>

{#if selected}
    {#each inputs as _, i}
        <input type="text" placeholder={selected.input_info[i]} bind:value={inputs[i]} data-index={i} on:input={onInput}>
    {/each}
{/if}