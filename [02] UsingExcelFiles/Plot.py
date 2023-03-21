import matplotlib.pyplot as plt
import xlrd


def plot():
	wb = xlrd.open_workbook(r"result.xlsx")
	# wb = xlrd.open_workbook(r"res-sig7.08-size9800m.xlsx")
	sheet = wb.sheet_by_index(0)
	adr_methodes = []
	mob_PDR_values = []
	mob_energy_values = []
	sta_PDR_values = []
	sta_energy_values = []

	num_adr = 4
	num_node_count = 7
	for i in range(num_adr):
		adr_methodes.append("")
		mob_PDR_values.append([])
		mob_energy_values.append([])
		sta_PDR_values.append([])
		sta_energy_values.append([])
		for j in range(0,num_node_count):
			mob_PDR_values[i].append(0)
			mob_energy_values[i].append(0)
			sta_PDR_values[i].append(0)
			sta_energy_values[i].append(0)


	row_idx = 4
	col_idx = ord('C') - ord('A')
	for i in range(0,num_adr):
		adr_methodes[i] = sheet.cell(row_idx+i, col_idx-2).value
		for j in range(0,num_node_count):
			col_idx = ord('C') - ord('A')
			sta_PDR_values[i][j] = sheet.cell(row_idx+i, col_idx+j).value
			sta_energy_values[i][j] = sheet.cell(row_idx+i, col_idx+j+8).value
			col_idx = ord('S') - ord('A')
			mob_PDR_values[i][j] = sheet.cell(row_idx+i, col_idx+j).value
			mob_energy_values[i][j] = sheet.cell(row_idx+i, col_idx+j+8).value

	x_range = [i*100 for i in range(1,num_node_count+1)]
	color_arr = ['blue', 'red', 'cyan', 'black', 'yellow', 'green', 'orange']
	line_arr = ['1', 'v', '^', '>', '<', ',', '.']

	plt.rcParams['axes.grid'] = True
	fig = plt.figure(figsize=(15, 8))
	fig.suptitle("Node Number Effect - Suburban vs Urban - sigma:7.08, 3.56 ")
	ax1 = fig.add_subplot(221)
	ax2 = fig.add_subplot(222)
	ax3 = fig.add_subplot(223)
	ax4 = fig.add_subplot(224)


	for i in range (num_adr):
		ax1.plot(x_range, sta_PDR_values[i], linestyle='dashed',\
			marker='{}'.format(line_arr[i]), \
			color='{}'.format(color_arr[i]), label='Sub_{}'.format(adr_methodes[i]))
	ax1.set(xlabel='Node Number', ylabel='Packet Delivery Ratio (%)')
	ax1.legend(loc='best')

	for i in range (num_adr):
		ax2.plot(x_range, sta_energy_values[i], linestyle='dashed',\
			marker='{}'.format(line_arr[i]), \
			color='{}'.format(color_arr[i]), label='Sub_{}'.format(adr_methodes[i]))
	ax2.set(xlabel='Node Number', ylabel='Total Energy Consumerd (KJ)')
	ax2.legend(loc='best')


	for i in range (num_adr):
		ax3.plot(x_range, mob_PDR_values[i], linestyle='solid',\
			marker='{}'.format(line_arr[i]), \
			color='{}'.format(color_arr[i]), label='Urb_{}'.format(adr_methodes[i]))
	ax3.set(xlabel='Node Number', ylabel='Packet Delivery Ratio (%)')
	ax3.legend(loc='best')


	for i in range (num_adr):
		ax4.plot(x_range, mob_energy_values[i], linestyle='solid',\
			marker='{}'.format(line_arr[i]), \
			color='{}'.format(color_arr[i]), label='Urb_{}'.format(adr_methodes[i]))
	ax4.set(xlabel='Node Number', ylabel='Total Energy Consumerd (KJ)')
	ax4.legend(loc='best')
	

	# xlim = [90, 710]
	# ylim = [0,100]
	# ax1.set_xlim(xlim)
	# ax1.set_ylim(ylim)
	# ax2.set_xlim(xlim)
	# # ax2.set_ylim(ylim)
	# ax3.set_xlim(xlim)
	# ax3.set_ylim(ylim)
	# ax4.set_xlim(xlim)
	# ax4.set_ylim(ylim)

	plt.show()
plot()