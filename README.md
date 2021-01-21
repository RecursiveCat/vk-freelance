# vk-freelance
<h3>class Exel</h3>

Example demo:<br>
exel = Exel("/home/int0x80/Public/vk-freelance/tables/test.csv")<br>
print(exel.get_row_from_table(1))<br>
exel.write_row_to_csv([1,2,3],"lol.csv")<br>
print(exel.get_last_written_row())<br>
print(exel.get_last_exported_row())<br>
print(exel.find_symbols_in_row("https",exel.get_last_exported_row()))<br>

Methods:<br>
Exel.__init__(self,"/path/to/your/csv/file.csv") -> self <br>
Exel.get_last_writed_row()                       -> list <br>
Exel.get_last_exported_row()                     -> list <br>
Exel.find_symbols_in_row("Text to find",[any array with dump etc]) -> bool <br>
Exel.get_row_from_table(int(row num/index ))     -> list <br>
Exel.get_path_to_csv_table
