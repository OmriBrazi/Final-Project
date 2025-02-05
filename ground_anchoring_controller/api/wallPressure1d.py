from numpy import * 
from copy import deepcopy


# presure formula=> P = phg
p= 997   # water mass density = 997 kg/m³
g = 9.8 # 9.8 m/sec^2 


# Done !
'''
# inputs  => height :number 
# output  => wall presure without anchors "floatList"
# p1 List
'''
def create_mat_wall_presure1d(height ):
    wall_presure = []
    for h in range(0,height+1):
        presure = p*g*h
        wall_presure.append(presure) 
    return wall_presure
 
   
# Done !
'''
  inputs  => (height : number) , (wall_presure : floatList) , (anchors : array of {id:number , x:number , y:number})
  output  => wall presure with the anchors "floatList"
'''
def calculate_mat_wall_presure1d(height , wall_presure , anchors):
    
    wall_presure2 = wall_presure.copy()
    for anchor in anchors:     
        y = anchor['y']       
    # distance = 0
        wall_presure2[y] = 0
    # distance = 1
        if(y+1 <height):
            wall_presure2[y+1] = wall_presure2[y+1]*0.25
        if(y-1 >0):
            wall_presure2[y-1] = wall_presure2[y-1]*0.25       
    # distance = 2   
        if(y+2 <height):
            wall_presure2[y+2] = wall_presure2[y+2]*0.5
        if(y-2 >0):
            wall_presure2[y-2] = wall_presure2[y-2]*0.5       
    # distance = 3
        if(y+3 <height):
            wall_presure2[y+3] = wall_presure2[y+3]*0.75
        if(y-3 >0):
            wall_presure2[y-3] = wall_presure2[y-3]*0.75
    return wall_presure2


# Done !
'''
    this function should to put the anchors in good place 
    inputs  => (height : number) , 
    output  => anchors 
    p2 matrix
'''
def create_best_anchors_for_wall_presure1d(height ):
    anchors =[]
    y1 = height-2
    id = 1
    while (y1 > 2 ):  
        anchors.append({'id' :id ,'x' :0 , 'y' :y1})
        y1-=2
        id+=1   
    return anchors
    

# Done !
def covert_matrix_presure_to_number1d(wall_presure):
    return sum(wall_presure)
 
    
# Done !
'''
    This function take ( p1 =the maxinum presure ,p2 = the minumum presure ,p3 = the current presure) 
    and calculate the quality between them in this way =>
    quality = (p1-p3)/(p1-p2)
    Inputs  => (p1 : number) , (p2 : number) , (p3 : number)
    Output  => (quality : number)
'''
def calculate_quality1d(p1 , p2 , p3):
    quality = 1- ((p3-p2)/(p1-p2))
    return quality
    

# Done !
def quality1d (height,anchors):
    # 1
    #print("1111")
    p1 = create_mat_wall_presure1d(height)   
    p1_sum = covert_matrix_presure_to_number1d(p1)
    
    
    # 2
    #print("2222")
    best_places_for_anchors = create_best_anchors_for_wall_presure1d(height )
    p2 = calculate_mat_wall_presure1d(height , deepcopy(p1) ,best_places_for_anchors)
    p2_sum = covert_matrix_presure_to_number1d(p2)
    # 3
    #print("3333")
    p3 = calculate_mat_wall_presure1d(height, p1 ,anchors)
    p3_sum = covert_matrix_presure_to_number1d(p3)
    
    return calculate_quality1d(p1_sum ,p2_sum ,p3_sum)
    