"""Tkinter front-end for the Shapes Calculator."""

from __future__ import annotations

import tkinter as tk
from tkinter import font, ttk

from .shapes import CATEGORIES, Measurement, ShapeError, ShapeSpec, shapes_in
from .units import DEFAULT_UNIT, UNITS, format_unit


def format_number(value: float) -> str:
    """Round to 4 decimals and drop pointless trailing zeros."""
    text = f"{value:,.4f}".rstrip("0").rstrip(".")
    return text or "0"


class ShapeCalculatorApp(ttk.Frame):
    """Main window: pick a shape, enter its dimensions, see the results."""

    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root, padding=14)
        self.root = root

        self.category_var = tk.StringVar(value=CATEGORIES[0])
        self.shape_var = tk.StringVar()
        self.unit_var = tk.StringVar(value=DEFAULT_UNIT)
        self.status_var = tk.StringVar()

        self._specs: list[ShapeSpec] = []
        self._input_vars: list[tk.StringVar] = []
        self._input_entries: list[ttk.Entry] = []
        self._unit_labels: list[ttk.Label] = []

        self._setup_styles()
        self._build_widgets()
        self._on_category_change()

        self.pack(fill="both", expand=True)
        self.root.bind("<Return>", lambda _event: self._calculate())

    def _setup_styles(self) -> None:
        self._title_font = font.nametofont("TkDefaultFont").copy()
        self._title_font.configure(size=16, weight="bold")
        style = ttk.Style(self)
        style.configure("Title.TLabel", font=self._title_font)
        style.configure("Error.TLabel", foreground="#b00020")
        style.configure("Note.TLabel", foreground="#1b5e20")

    def _build_widgets(self) -> None:
        ttk.Label(self, text="Shapes Calculator", style="Title.TLabel").pack(anchor="w")

        chooser = ttk.LabelFrame(self, text="Choose a shape", padding=10)
        chooser.pack(fill="x", pady=(10, 0))
        chooser.columnconfigure(1, weight=1)

        ttk.Label(chooser, text="Category:").grid(row=0, column=0, sticky="w", pady=2)
        category_combo = ttk.Combobox(
            chooser, textvariable=self.category_var,
            values=list(CATEGORIES), state="readonly",
        )
        category_combo.grid(row=0, column=1, sticky="ew", padx=(8, 0), pady=2)
        category_combo.bind("<<ComboboxSelected>>", lambda _e: self._on_category_change())

        ttk.Label(chooser, text="Shape:").grid(row=1, column=0, sticky="w", pady=2)
        self.shape_combo = ttk.Combobox(
            chooser, textvariable=self.shape_var, state="readonly",
        )
        self.shape_combo.grid(row=1, column=1, sticky="ew", padx=(8, 0), pady=2)
        self.shape_combo.bind("<<ComboboxSelected>>", lambda _e: self._on_shape_change())

        ttk.Label(chooser, text="Unit:").grid(row=2, column=0, sticky="w", pady=2)
        unit_combo = ttk.Combobox(
            chooser, textvariable=self.unit_var,
            values=list(UNITS), state="readonly",
        )
        unit_combo.grid(row=2, column=1, sticky="ew", padx=(8, 0), pady=2)
        unit_combo.bind("<<ComboboxSelected>>", lambda _e: self._on_unit_change())

        self.inputs_frame = ttk.LabelFrame(self, text="Dimensions", padding=10)
        self.inputs_frame.pack(fill="x", pady=(10, 0))
        self.inputs_frame.columnconfigure(1, weight=1)

        buttons = ttk.Frame(self)
        buttons.pack(fill="x", pady=(10, 0))
        ttk.Button(buttons, text="Calculate", command=self._calculate).pack(side="left")
        ttk.Button(buttons, text="Clear", command=self._clear).pack(side="left", padx=8)

        self.status_label = ttk.Label(
            self, textvariable=self.status_var, wraplength=460, style="Note.TLabel",
        )
        self.status_label.pack(fill="x", pady=(8, 0), anchor="w")

        results_frame = ttk.LabelFrame(self, text="Results", padding=10)
        results_frame.pack(fill="both", expand=True, pady=(10, 0))
        self.results = ttk.Treeview(
            results_frame, columns=("property", "value"),
            show="headings", height=8, selectmode="none",
        )
        self.results.heading("property", text="Property")
        self.results.heading("value", text="Value")
        self.results.column("property", width=230, anchor="w")
        self.results.column("value", width=180, anchor="e")
        self.results.pack(fill="both", expand=True)

    def _on_category_change(self) -> None:
        self._specs = shapes_in(self.category_var.get())
        self.shape_combo["values"] = [spec.name for spec in self._specs]
        self.shape_var.set(self._specs[0].name)
        self._on_shape_change()

    def _on_shape_change(self) -> None:
        self._rebuild_inputs(self._current_spec())
        self._clear_results()
        self._set_status("")

    def _on_unit_change(self) -> None:
        symbol = format_unit(self.unit_var.get())
        for label in self._unit_labels:
            label.configure(text=symbol)
        if self.results.get_children():  # refresh visible results
            self._calculate()

    def _current_spec(self) -> ShapeSpec:
        name = self.shape_var.get()
        return next(spec for spec in self._specs if spec.name == name)

    def _rebuild_inputs(self, spec: ShapeSpec) -> None:
        for child in self.inputs_frame.winfo_children():
            child.destroy()
        self._input_vars.clear()
        self._input_entries.clear()
        self._unit_labels.clear()

        symbol = format_unit(self.unit_var.get())
        for row, field_name in enumerate(spec.fields):
            var = tk.StringVar()
            ttk.Label(self.inputs_frame, text=f"{field_name}:").grid(
                row=row, column=0, sticky="w", pady=3)
            entry = ttk.Entry(self.inputs_frame, textvariable=var)
            entry.grid(row=row, column=1, sticky="ew", padx=8, pady=3)
            unit_label = ttk.Label(self.inputs_frame, text=symbol, width=4)
            unit_label.grid(row=row, column=2, sticky="w")

            self._input_vars.append(var)
            self._input_entries.append(entry)
            self._unit_labels.append(unit_label)

        if self._input_entries:
            self._input_entries[0].focus_set()

    def _read_inputs(self, spec: ShapeSpec) -> list[float]:
        values: list[float] = []
        for field_name, var in zip(spec.fields, self._input_vars):
            try:
                values.append(float(var.get().strip()))
            except ValueError:
                raise ShapeError(f"“{field_name}” must be a number.") from None
        return values

    def _calculate(self) -> None:
        spec = self._current_spec()
        try:
            shape = spec.create(*self._read_inputs(spec))
            measurements = shape.measurements()
            note = shape.description()
        except ShapeError as error:
            self._clear_results()
            self._set_status(str(error), is_error=True)
            return

        self._show_results(measurements)
        self._set_status(f"Detected: {note}" if note else "")

    def _show_results(self, measurements: list[Measurement]) -> None:
        self._clear_results()
        unit_name = self.unit_var.get()
        for item in measurements:
            unit = format_unit(unit_name, item.dimension)
            self.results.insert(
                "", "end", values=(item.label, f"{format_number(item.value)} {unit}"),
            )

    def _clear(self) -> None:
        for var in self._input_vars:
            var.set("")
        self._clear_results()
        self._set_status("")
        if self._input_entries:
            self._input_entries[0].focus_set()

    def _clear_results(self) -> None:
        self.results.delete(*self.results.get_children())

    def _set_status(self, message: str, *, is_error: bool = False) -> None:
        self.status_var.set(message)
        self.status_label.configure(style="Error.TLabel" if is_error else "Note.TLabel")


def main() -> None:
    root = tk.Tk()
    root.title("Shapes Calculator")
    root.minsize(500, 640)
    ShapeCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
