import csv

th = "[tps_header]"
th_e = "[/tps_header]" 
tt = "[tps_title]"
tt_e = "[/tps_title]"
np = "<!--nextpage-->"
enter = "\n"

def generate_image_anchor(title,image_path,image_alt,image_num,page_number):
  a = "<a href=\"http://brainsmuggler.com/slideshows/"+title+"/"+page_number+"/\"><img class=\"aligncenter size-single-thumb wp-image-"+image_num+"\" src=\"http://brainsmuggler.com/wp-content/"+image_path+"\" alt=\""+image_alt+"\" width=\"620\" height=\"379\" /><p class=\"wp-caption-text\">Source: Shutterstock</p>"
  return a

def generate_header():
  content = th+th_e
  print(content)

def generate_slide(show_title,slide_title,image_path,image_alt,image_num,slide_number,slide_content):
  content = tt + slide_title + tt_e + enter + generate_image_anchor(show_title,image_path,image_alt,image_num,slide_number) + enter + slide_content + enter + np
  print(content)

with open('slideshow.csv','rb') as csvfile:
        q_reader = csv.DictReader(csvfile,delimiter=',')
        for row in q_reader:
	  generate_slide(row['show_title'],row['slide_title'],row['image_path'],row['image_alt'],row['image_num'],row['slide_number'],row['slide_content'])
