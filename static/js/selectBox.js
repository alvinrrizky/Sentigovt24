window.Components = {
    customSelect(options) {
        return {
            init() {
                this.$refs.listbox.focus()
                this.optionCount = this.$refs.listbox.children.length
                this.$watch('selected', value => {
                    if (!this.open) return

                    if (this.selected === null) {
                        this.activeDescendant = ''
                        return
                    }

                    this.activeDescendant = this.$refs.listbox.children[this.selected - 1].id
                })
            },
            activeDescendant: null,
            optionCount: null,
            open: false,
            selected: null,
            value: 1,
            choose(option) {
                this.value = option
                this.open = false
            },
            onButtonClick() {
                if (this.open) return
                this.selected = this.value
                this.open = true
                this.$nextTick(() => {
                    this.$refs.listbox.focus()
                    this.$refs.listbox.children[this.selected - 1].scrollIntoView({
                        block: 'nearest'
                    })
                })
            },
            onOptionSelect() {
                if (this.selected !== null) {
                    this.value = this.selected
                }
                this.open = false
                this.$refs.button.focus()
            },
            onEscape() {
                this.open = false
                this.$refs.button.focus()
            },
            onArrowUp() {
                this.selected = this.selected - 1 < 1 ? this.optionCount : this.selected - 1
                this.$refs.listbox.children[this.selected - 1].scrollIntoView({
                    block: 'nearest'
                })
            },
            onArrowDown() {
                this.selected = this.selected + 1 > this.optionCount ? 1 : this.selected + 1
                this.$refs.listbox.children[this.selected - 1].scrollIntoView({
                    block: 'nearest'
                })
            },
            ...options,
        }
    },
}