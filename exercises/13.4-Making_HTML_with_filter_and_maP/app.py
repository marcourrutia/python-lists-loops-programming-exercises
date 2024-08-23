all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def generate_li(color):
    return f'<li>{color["label"]}</li>'

def filter_colors(colors):
    return colors["sexy"]

filtered_color = list(map(generate_li,filter(filter_colors, all_colors)))
print(filtered_color)