import math
from PIL import Image, ImageDraw
import time
#create an empty new image (image is nxm size)
n=841   
m=594



#------------------------arrange the polygons in decending acording to thr area
def arrangeInDecendingOrder(Allshapes,shape_name):
    area=list()
    for poly in Allshapes:
        tem=polygonArea(poly)
        area.append(tem)
    n=len(area)
    for i in range(n):
        for j in range((n-i-1)):
            if(area[j]<area[j+1]):
                grtr=area[j+1]
                area[j+1]=area[j]
                area[j]=grtr
                
                p=Allshapes[j+1]
                Allshapes[j+1]=Allshapes[j]
                Allshapes[j]=p
                
                z=shape_name[j+1]
                shape_name[j+1]=shape_name[j]
                shape_name[j]=z
    return Allshapes , shape_name

#--------------------------------------------rotate a point at particular angle
def rotate_point(origin,point,angle):
    ox,oy=origin
    px,py=point
    angle=math.radians(angle)
    
    qx=ox+math.cos(angle)*(px-ox)-math.sin(angle)*(py-oy)
    qy=oy+math.sin(angle)*(px-ox)+math.cos(angle)*(py-oy)
    return qx,qy

#------------------------------------------------------------------------------
def chck_point_in_polygons_2(poly_set,pnt):
    from shapely.geometry import Polygon,Point
    flag=0
    pnt=Point(pnt)
    for poly in poly_set:
        poly=Polygon(poly)
        if(pnt.within(poly)):        
            flag=1                                      
            break
    if(flag==0):
        return True
    else:
        return False
#------------------------------------------------------------------------------
def check_polygon_intersect_polygons(polygons,polygon):
    flag=0
    for poly in polygons:
         if(check_polygon_intersect_1(poly,polygon)):
             flag=1
             break
    if(flag==0):
        return False
    else:
        return True
#-------------------------------------------------------------------------------
#def check_polygon_intersect_circle(plygon,circle):
def check_polygon_intersect_1(p1,p2):
    from shapely.geometry import Polygon
    p1=Polygon(p1)
    p2=Polygon(p2)
    return (p1.intersects(p2))
        
#-------------------------------------------------function to rotate a polygon
def rotate_polygon(origin,polygon,angle):
    poly=list.copy(polygon)
    i=0
    for point in poly:
        poly[i]=rotate_point(origin,point,angle)
        i=i+1
    return poly
#----------------------------------create a function that will generate polygon
def draw_polygon(lines,name,draw,im,tim):
    i=-1
    
    if(len(lines)>10):
        tim=5
        print("ye")
    else:
        tim=50
    
    name=name+'.png'
    pnt_2=[1,2]
    pnt_1=[1,2]
    for point in lines:
        #edited
        pnt_2[0]= lines[i][0]*precesion
        pnt_2[1]=lines[i][1]*precesion
        
        pnt_1[0]=point[0]*precesion
        pnt_1[1]=point[1]*precesion
        
        #end edited
        a=tuple(pnt_2)+tuple(pnt_1)
        i=i+1
        #draw.line((a),width=3,fill=128)
        draw.line((a))
    im.save(name)
    '''
        npimage=cv2.imread(name)
        cv2.imshow('image',npimage)
        cv2.waitKey(1000)
    '''
#-----------------------------------------------------------------------------
def copy_paste(number):
    
    name=str(number-1)+'.png'
    
    #img=cv2.imread(name)
    img=Image.open(name)
    name=str(number)+'.png'
    #cv2.imwrite(name,img)
    img.save(name)
    
#------------------------------------check for the intersection of segment line

#-------------------------------------------------------------shifting position
def shift_centroid(poly,centroid):
    pol=list.copy(poly)
    #print(type(centroid))
    new_poly=list()
    z=0
    for point in pol:
        #point[0]=point[0]+centroid[0]
        #point[1]=point[1]+centroid[1]
        x=poly[z][0]+centroid[0]
        y=poly[z][1]+centroid[1]
        new_poly.append([x,y])
        z=z+1
    return new_poly
#----------------------------------------check for the intersection b/w polygon

#-------------------------------------------------Calculate the area of polygon
def polygonArea(polygon): 
    X=list()
    Y=list()
    
    for point in polygon:
        X.append(point[0])
        Y.append(point[1])
        
    n=len(X)
    # Initialze area 
    area = 0.0
  
    # Calculate value of shoelace formula 
    j = n - 1
    for i in range(0,n): 
        area += (X[j] + X[i]) * (Y[j] - Y[i]) 
        j = i   # j is previous vertex to i 
      
  
    # Return absolute value 
    return int(abs(area / 2.0)) 
#----------------function-1 that will take all_shapes and will generate image------------------------------
#----------------------------------------------------------------------------------------------function 6
def calulate_efficienct_6(all_shapes,nem,shape_name,current_elem,current_po):  
    name=str(nem)
    #current_elem=list()
    area_draw=0                         #variable use to store the area of total polygons
    im = Image.new('RGB', (n*precesion, m*precesion))
    draw = ImageDraw.Draw(im)

    
    #all_shapes , shape_name=arrangeInDecendingOrder(all_shapes,shape_name)
    print("phase 1 ")
    plain_elem=[[[0,0],[0,m],[-1,m],[-1,0]],[[0,0],[n,0],[n,-1],[0,-1]],[[0,m],[n,m],[n,m+1],[0,m+1]],[[n,0],[n,m],[n+1,m],[n+1,0]]]
    centr=[0,0]
    count=0             
    flag=0          
    first_shape=1  
    flag_2=0
    flag_3=0
    sh_nm="abc"
    
#-------------------------------------------checking for existance
    #poly and cur_elem is the name 
    cout_2=0
    current_elem_2=list()
    if(name!='1'):
        print("Comparing with last sheet")
        for cur_elem in current_elem:
            flg=0
            cout=0
            shape_name_1=list.copy(shape_name)  #All shapes name
            for poly in shape_name_1: 
                if(cur_elem==poly):
                    area_draw=area_draw+polygonArea(all_shapes[cout])  #calcualte area from any poly
                    #draw_polygon(current_po[cout_2],name,draw,im)      #draw from previous 
                    current_elem_2.append(poly)                        #adding current drawing shapes name 
                    b=plain_elem                                       
                    b.append(current_po[cout_2])                       #adding current drawing shape dimention 
                    plain_elem=b      
                    all_shapes.remove(all_shapes[cout])
                    #all_shapes=delete(all_shapes,cout,axis=0)          #deleting shape dimention from all elemet 
                    shape_name.remove(shape_name[cout])
                    #shape_name=delete(shape_name,cout,axis=0)          #deleting shape name from shape_name 
                    flg=1
                    break
                cout=cout+1
            cout_2=cout_2+1
            if(flg==0):
                break
        #current_elem=current_elem_2
#------------------------------------------------------------------------------
    pt_a=0
    pt_b=3
    last=""
    if(name=='1'or (len(current_elem)!=len(current_elem_2))): 
        for poly in plain_elem[4:]:
            draw_polygon(poly,name,draw,im,70)
        #shape_name_copy=shape_name    
        all_shapes_1=list.copy(all_shapes)                     
        for poly in all_shapes_1:  
            
            current_elem=current_elem_2
            #first loop start
            flag_2=0
            flag_3=0
            print("check------"+shape_name[count])  #edited
            if(sh_nm==shape_name[count]):
                count=count+1
                continue
            
            
            print(shape_name[count]+"-----------"+last)
            if(last==shape_name[count]):
                #y=centr[0]
                #x=centr[1]
                x=pt_a
                y=pt_b
                print("---------------"+str(x)+","+str(y))
            else:
                x=0
                y=3
                pt_a=0
                pt_b=3
            
            print("Going through--------------"+shape_name[count])   #edited
            
            global anglee
            i_2=anglee
            if(shape_name[count][:7]=='hexagon'):
                angl=60
                #i=15
            elif(shape_name[count][:6]=='circle'):
                angl=1
                #i=15
            elif(shape_name[count][:7]=='ellipse'):
                angl=100  #original 180 befr 90
                #i=30
            elif(shape_name[count][:9]=='rectangle'):
                angl=180
                #i=15
            elif(shape_name[count][:8]=='pentagon'):
                angl=72
                #i=15
            elif(shape_name[count][:4]=='kite'):
                angl=180
                #i=15
            elif(shape_name[count][:8]=='triangle'):
                angl=361    #changed from 360 to 180
                #i=15
            elif(shape_name[count][:9]=='trapezium'):
                angl=361                   #changed from 360 to 180
                i_2=180
            elif(shape_name[count][:19]=='equlateral triangle'):
                angl=120
                            
            
            
            flag_2=0                                                                                                        
            for j in range(y,m,10):
                #second loop start    
                #x=pt_a                                                  
                for i in range(0,n,10):
                    #third loop start
                    centr[0]=i
                    centr[1]=j
                    if(chck_point_in_polygons_2(plain_elem[4:],centr)==True or first_shape==1):
                            #first if start
                            pol=shift_centroid(poly,centr)
                            for angle in range(0,angl,i_2):
                                #fourth loop start
                                po=rotate_polygon(centr,pol,angle)
                                if(check_polygon_intersect_polygons(plain_elem,po)==False):
                                     print("drawing----------------"+shape_name[count])
                                     #print(shape_name[count])   #edited
                                     #print(po)
                                     pt_a=i
                                     pt_b=j
                                     area_draw=area_draw+polygonArea(po)
                                     
                                     #b=plain_elem                                       
                                     #b.append(po)
                                     current_elem.append(shape_name[count]) #edited
                                     plain_elem.append(po)          
                                     
                                     draw_polygon(po,name,draw,im,30)                                  
                                     #all_shapes=delete(all_shapes,count,axis=0)
                                     all_shapes.remove(all_shapes[count])
                                     last=shape_name[count]
                                     #shape_name=delete(shape_name,count,axis=0)
                                     shape_name.remove(shape_name[count])
                                     
                                     flag=1
                                     flag_2=1       
                                     flag_3=1
                                     first_shape=0
                                     break
                                #fourth loop ends here
                            #first if ends here
                    if(flag==1):
                        break
                    #third loop ends here
                if(flag==1):
                    break
                #second loop ends here
            
            if(flag_3==0):
                print("yeah its geting")
                sh_nm=shape_name[count]
            
            if(flag_2==0):        
                count=count+1
            flag=0
            
            
            #first loop ends here
    else:
        copy_paste(nem)
        
    print("-----------------------------------")#edited
    #print(all_shapes)
    #cv2.waitKey(100)
    #cv2.destroyAllWindows()
    name=int(name)
    name=name+1
    efficiency=(area_draw/(m*n))*100
    print("EFICIENCY="+str(efficiency)+"%")
    all_efficiency.append(efficiency)
    pages=0
    eff=0
    if(len(all_shapes)>0):
        pages,eff=calulate_efficienct_6(all_shapes,name,shape_name,current_elem,plain_elem[4:])
    pages=pages+1
    efficiency=efficiency+eff
    
    return pages,efficiency

#------------------------------------------------------------------------------this function will generate shapes

def generate_shapes():
    import shapely.affinity
    from shapely.geometry import Point
    circle = Point(0, 0).buffer(1) 
    
    ellipse_1 = shapely.affinity.scale(circle, 50, 150)                                           #ellipse_1
    ellipse_1=list(zip(*ellipse_1.exterior.coords.xy))                                          
    ellipse_2=shapely.affinity.scale(circle, 90, 180)                                             #ellipse_2
    ellipse_2=list(zip(*ellipse_2.exterior.coords.xy))
    circle_1=shapely.affinity.scale(circle, 120, 120)                                             #circle_1
    circle_1=list(zip(*circle_1.exterior.coords.xy))
    circle_2=shapely.affinity.scale(circle, 107, 107)                                             #circle_2
    circle_2=list(zip(*circle_2.exterior.coords.xy))
    shape_5=[[-175,0],[-87.5,151.55],[87.5,151.55],[175,0],[87.5,-151.55],[-87.5,-151.55]] #hexagon
    shape_6=[[-75,90],[75,90],[75,-90],[-75,-90]]                                        #rectrangle_1
    shape_7=[[-100,70],[100,70],[100,-70],[-100,-70]]                                 #rectrangle_2
    shape_8=[[-161.8,52.5],[0,170.1],[161.8,52.57],[100,-137.6],[-100,-137.6]]             #pentagone
    shape_9=[[-100,0],[0,125],[100,0],[0,-125]]                                          #kite_1  
    shape_10=[[-75,0],[0,90],[75,0],[0,-90]]                                               #kite_2
    shape_11=[[-110,0],[0,100],[110,0],[0,-100]]                                           #kite_3
    shape_12=[[-150,-50],[0,100],[150,-50]]                                                #triangle_1
    shape_13=[[-95,-54.84],[0,109.69],[95,-54.84]]                                         #triangle_2
    shape_14=[[-90,-83.5],[-60,83.5],[60,83.5],[90,-83.5]]                                 #trapizium_1 
    shape_15=[[-90,-92.5],[-60,92.5],[60,92.5],[90,-92.50]]                                #trapizium_2

    
    shapes=[circle_1,circle_2,ellipse_1,ellipse_2,shape_5,shape_6,shape_7,shape_8,shape_9,shape_10,shape_11,shape_12,shape_13,shape_14,shape_15]
    names=["circle1","circle2","ellipse1","ellipse2","hexagon1","rectangle1","rectangle2","pentagon1","kite1","kite2","kite3","triangle1","equlateral triangle1","trapezium1","trapezium2"]
    return shapes,names

#-----------------------------------------------------------------------------
def user_interface():
    ttl=4
    #point=[0,0]
    polygon=list()
    polygons=list()
    names=list()
    flag_1=0
    flag_2=0
    while(True):
        print()
        print("Enter your choice-")
        if(flag_1==0 and flag_2==0):
            print("     Enter 1 to use predefined set")
        if(flag_2==0):
            if(flag_1==0):
                print("     Enter 2 to create a set")
            else:
                print("     Enter 2 to add more shapes in a set")
        print("     Enter 3 to show the selected shapes")
        print("     Enter 4 to calculate the efficiency")
        print("     Enter 5 to exit")
        b=input(">>")
        if(b=='1'):
            flag_2=1
            polygons,names=generate_shapes()
        elif(b=='2'):
            
            while(True):
                print()
                print("Enter 1 to add hexagon")
                print("Enter 2 to add pentagon")
                print("Enter 3 to add circle")
                print("Enter 4 to add ellipse")
                print("Enter 5 to add rectangle")
                print("Enter 6 to add kite")
                print("Enter 7 to add trapezium")
                print("Enter 8 to add triangle")
                print("Enter 9 to go back")
                b=input(">>")
                
                
                if(b=='1'):
                    flag_1=1
                    ttl=ttl+1
                    polygon=[]
                    side=float(input("Enter the length of the side= "))
                    for i in range(0,360,60):
                        x=round(side*math.cos(math.radians(i)),2)
                        y=round(side*math.sin(math.radians(i)),2)
                        polygon.append([x,y])
                    polygons.append(polygon)
                    print(polygon)
                    names.append("hexagon"+str(ttl))
                elif(b=='2'):
                    flag_1=1
                    ttl=ttl+1
                    polygon=[]
                    side=float(input("Enter the length of the side= "))
                    side=side/(2*math.cos(math.radians(54)))
                    for i in range(0,360,72):
                        x=round(side*math.cos(math.radians(i)),2)
                        y=round(side*math.sin(math.radians(i)),2)
                        polygon.append([x,y])
                    polygons.append(polygon)
                    names.append("pentagon"+str(ttl))
                    print(polygons)
                elif(b=='3'):
                    flag_1=1
                    ttl=ttl+1
                    polygon=[]
                    radius=float(input("Enter the radius of the circle= "))
                    import shapely.affinity
                    from shapely.geometry import Point
                    circle = Point(0, 0).buffer(1) 
                    polygon = shapely.affinity.scale(circle, radius, radius)
                    polygon=list(zip(*polygon.exterior.coords.xy))   
                    polygons.append(polygon)
                    names.append("circle"+str(ttl))
                elif(b=='4'):
                    flag_1=1
                    ttl=ttl+1
                    polygon=[]
                    maj_axis=(float(input("Enter the length of major axis= ")))/2
                    min_axis=(float(input("Enter the length of the minor axis= ")))/2
                    import shapely.affinity
                    from shapely.geometry import Point
                    circle = Point(0, 0).buffer(1) 
                    polygon = shapely.affinity.scale(circle, maj_axis, min_axis)
                    polygon=list(zip(*polygon.exterior.coords.xy))   
                    polygons.append(polygon)
                    names.append("ellipse"+str(ttl))
                elif(b=='5'):
                    flag_1=1
                    ttl=ttl+1
                    polygon=[]
                    length=float(input("Enter the length= "))
                    breath=float(input("Enter the breath= "))
                    polygon=[[length/2,-breath/2],[length/2,breath/2],[-length/2,breath/2],[-length/2,-breath/2]]
                    polygons.append(polygon)
                    names.append("rectangle"+str(ttl))
                elif(b=='6'):
                    flag_1=1
                    ttl=ttl+1
                    polygon=[]
                    length=float(input("Enter the length of first diagonal=  "))
                    breath=float(input("Enter the length of second diagonal= "))
                    polygon=[[length/2,0],[0,breath/2],[-length/2,0],[0,-breath/2]]
                    polygons.append(polygon)
                    names.append("kite"+str(ttl))
                elif(b=='7'):
                    flag_1=1
                    ttl=ttl+1
                    polygon=[]
                    height=float(input("Enter the height = "))
                    sht_side=float(input("Enter the length of the shorter side= "))
                    long_side=float(input("Enter the length of the longer side= "))
                    polygon=[[long_side/2,-height/2],[sht_side/2,height/2],[-sht_side/2,height/2],[-long_side/2,-height/2]]
                    polygons.append(polygon)
                    names.append("trapezium"+str(ttl))
                elif(b=='8'):
                    flag_1=1
                    ttl=ttl+1
                    polygon=[]
                    a=float(input("Enter the first side  = "))
                    b=float(input("Enter the second side = "))
                    c=float(input("Enter the third side  = "))
                    
                    cosa=(b*b+c*c-a*a)/(2*b*c)
                    x=b*cosa
                    y=round(b*math.sin((math.acos(cosa))),4)
                    vtx_1=[0,0]
                    vtx_2=[c,0]
                    vtx_3=[x,y]
                    polygon=[vtx_1,vtx_2,vtx_3]
                    centroid=[-((vtx_1[0]+vtx_2[0]+vtx_3[0])/3),-((vtx_1[1]+vtx_2[1]+vtx_3[1])/3)]
                    polygon=shift_centroid(polygon,centroid)
                    polygons.append(polygon)
                    if(a==b and b==c and c==a):
                        names.append("equlateral triangle"+str(ttl))
                    else:
                        names.append("triangle"+str(ttl))
                elif(b=='9'):
                    break
                else:
                    print("Enter the correct choice")                    
            
        elif(b=='3'):
            if(len(names)==0):
                print("You have not selected any shapes yet")
            else:
                print("--------------------------")
                for shp in names:
                    print(shp)
                print("--------------------------")
        elif(b=='4'):
            if(len(names)==0):
                print("You have not selected any shapes.")
            else:
                print("Do you want to fit the shapes in the default sheet (849mm x 594mm) ?")
                ans=input("Type y for yes or n for no= ")
                while(True):
                    if(ans=='y' or ans=='Y'):
                        pass
                    elif(ans=='n' or ans=='N'):
                        global m
                        global n
                        m=int(input("Enter the length of the sheet"))
                        n=int(input("Enter the breath of the sheet"))
                    else:
                        print("Enter the correct choice")
                        continue
                    #----------------------------------------------------------------------------------------
                    
                    total_set=int(input("Enter the total number of sets you want to print for=  "))
                    global precesion
                    precesion=int(input("Enter total no of pixel per mm (default value is 1)=  "))
                    global anglee
                    anglee=int(input("Enter the angle precesion in degree (default value is 30)=  "))
                    
                    polygons_1=list()
                    names_1=list()
                    for i in range(0,total_set):
                        for poly in polygons:
                            polygons_1.append(poly)
                        for nam in names:
                            names_1.append(nam) 
                    
                    
                    start_time = time.time()
                    all_names=list()
                    current_elem_1=list()
                    polyee=list()
                    overall_shapes,all_names=arrangeInDecendingOrder(polygons_1,names_1)
                    page,eficienct=calulate_efficienct_6(overall_shapes,1,all_names,current_elem_1,polyee)
                    aff=eficienct/page

                    tim=round(((time.time() - start_time)/60),2)
                    print("=================================================")
                    print("\n\n---TOTAL TIME REQUIRED= %s minuites ---" %tim)
                    for i in range(0,page):
                        print("\n\nEfficiency for sheet "+str(i+1)+" is "+str(all_efficiency[i]))
                    print("-------------------------------------------------")
                    print("\n\nOverall efficiency=  "+str(aff)+"%")
                    #----------------------------------------------------------------------------------------------
                    return
                        
            
        elif(b=='5'):
            break
        else:
            print("Enter the correct choice")


all_efficiency=list()
precesion=1
anglee=30

user_interface()
jj=input("Enter to exit")









