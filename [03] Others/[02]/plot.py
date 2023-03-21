#!/usr/bin/env python
import matplotlib.pyplot as plt
import xlrd
from matplotlib.font_manager import FontProperties

font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 9}

plt.rc('font', **font)

def plot():
	wb = xlrd.open_workbook(r"Result - Urban.xlsx")
	title = "Urban Motionless Node Number Effect - sigma:3.56 - Radius: 480m"
	# wb = xlrd.open_workbook(r"Result - Suburban.xlsx")
	# title = "Suburban Motionless Node Number Effect - sigma:7.08 - Radius: 9800m"
	sheet = wb.sheet_by_index(0)
	adr_methodes = []
	PDR_values_1 = []
	energy_values_1 = []
	PDR_values_2 = []
	energy_values_2 = []
	x_axis = []

	num_adr = 5
	x_axis_count = 7
	for i in range(x_axis_count):
		x_axis.append('')
	for i in range(num_adr):
		adr_methodes.append("")
		PDR_values_1.append([])
		energy_values_1.append([])
		PDR_values_2.append([])
		energy_values_2.append([])
		for j in range(x_axis_count):
			PDR_values_1[i].append(0)
			energy_values_1[i].append(0)
			PDR_values_2[i].append(0)
			energy_values_2[i].append(0)



	row_idx = 1
	col_idx = ord('C') - ord('A')
	for i in range(x_axis_count):
		x_axis[i] = int(sheet.cell(row_idx, col_idx+i).value)

	row_idx = 2
	col_idx = ord('C') - ord('A')
	for i in range(num_adr):
		adr_methodes[i] = sheet.cell(row_idx+i, 0).value
		if (adr_methodes[i] == 'beni'):
			adr_methodes[i] = 'LP-MAB'
		elif (adr_methodes[i] == 'avg'):
			adr_methodes[i] = 'ADR-AVG[12]'
		elif (adr_methodes[i] == 'max'):
			adr_methodes[i] = 'ADR-MAX[15]'
		elif (adr_methodes[i] == 'No-ADR'):
			adr_methodes[i] = 'No-ADR[18]'
		for j in range(x_axis_count):
			col_idx = ord('C') - ord('A')
			PDR_values_1[i][j] = sheet.cell(row_idx+i, col_idx+j).value
			energy_values_1[i][j] = sheet.cell(row_idx+i, col_idx+j+(x_axis_count+1)).value
			# col_idx = ord('S') - ord('A')
			# mob_PDR_values[i][j] = sheet.cell(row_idx+i, col_idx+j).value
			# mob_energy_values[i][j] = sheet.cell(row_idx+i, col_idx+j+8).value


	color_arr = ['green', 'blue', 'red', 'red', 'black', 'green', '']
	line_type_arr = ['v', '^', 'x', 'x', 'o', '.']
	# line_style = ['dashed', 'dotted', 'dashdot', 'solid', 'dashdot']
	line_style = ['solid', 'solid', 'solid', 'solid', 'solid']

	plt.rcParams['axes.grid'] = True
	fig = plt.figure(figsize=(7.5, 5.5))
	
	fig.canvas.draw()
	# fig.suptitle(title)
	
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)
	# fig.tight_layout()
	# ax3 = fig.add_subplot(223)
	# ax4 = fig.add_subplot(224)

	
	for i in range (num_adr):
		if(adr_methodes[i] != 'owa'):
			ax1.plot(x_axis, PDR_values_1[i], 
				linestyle='{}'.format(line_style[i]),\
				marker='{}'.format(line_type_arr[i]), \
				# marker='^', \
				color='{}'.format(color_arr[i]), \
				# color='black', 
				label='{}'.format(adr_methodes[i]))
	
	ax1.set_xticks(x_axis)
	ax1.set_xticklabels(x_axis)
	ax1.set(xlabel='Number of Nodes', ylabel='Packet Delivery Ratio (%)')
	ax1.legend(loc='best')

	for i in range (num_adr):
		if(adr_methodes[i] != 'owa'):
			ax2.plot(x_axis, energy_values_1[i], 
				linestyle='{}'.format(line_style[i]),\
				marker='{}'.format(line_type_arr[i]), \
				# marker='^', \
				color='{}'.format(color_arr[i]),\
				# color='black', 
				label='{}'.format(adr_methodes[i]))
	ax2.set_xticks(x_axis)
	ax2.set_xticklabels(x_axis)
	ax2.set(xlabel='Number of Nodes', ylabel='Energy Consumption (mJ)')
	ax2.legend(loc='best')


	# for i in range (num_adr):
	# 	ax3.plot(x_range, mob_PDR_values[i], linestyle='solid',\
	# 		marker='{}'.format(line_type_arr[i]), \
	# 		color='{}'.format(color_arr[i]), label='Urb_{}'.format(adr_methodes[i]))
	# ax3.set(xlabel='Node Number', ylabel='Packet Delivery Ratio (%)')
	# ax3.legend(loc='best')


	# for i in range (num_adr):
	# 	ax4.plot(x_range, mob_energy_values[i], linestyle='solid',\
	# 		marker='{}'.format(line_type_arr[i]), \
	# 		color='{}'.format(color_arr[i]), label='Urb_{}'.format(adr_methodes[i]))
	# ax4.set(xlabel='Node Number', ylabel='Total Energy Consumerd (KJ)')
	# ax4.legend(loc='best')
	

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