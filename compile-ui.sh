for file in ./ui/*.ui
do
	pyside6-uic "$file" -o ./ui/$(basename "$file" .ui).py
done