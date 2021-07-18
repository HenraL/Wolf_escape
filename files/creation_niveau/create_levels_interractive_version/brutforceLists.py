for o in range(20):
    for v in range(23):
        i=o+1
        b=v+1
        print(f"self.alpha_L{i}_R{b} = StringVar()\nself.alpha_L{i}_R{b}.set(\"\")\nself.L{i}_R{b}=Entry(FrameL{i}, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief,text=self.alpha_L{i}_R{b})\nself.L{i}_R{b}.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)")
    print()
print("GridList=[")
for o in range(20):
    print("[",end="")
    for v in range(23):
        i=o+1
        b=v+1
        print(f"self.alpha_L{i}_R{b}",end=",")
    print("],")
print("\n]")
