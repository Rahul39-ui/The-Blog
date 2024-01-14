from django.shortcuts import render, redirect
from home.models import Blog
from datetime import date as Date
# Create your views here.
def index(request):
    
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        date = request.POST['date']
        if date == "":
            date = Date.today()
        ins = Blog(blog_title=title[0].upper()+title[1:], date=date, blog_content=content[0].upper() + content[1:])
        ins.save()
        
    
        
    return render(request, 'base.html')

def blogs(request):
    
    allBlogs = Blog.objects.all()
    blog_status = ""
    if Blog.objects.count() == 0:
        blog_status = "No Blogs"
        

        
    context = {
        'blogs': allBlogs,
        'blog_status': blog_status,
    }
    

    
    return render(request, "blogs.html", context)



def delete(request, id):
    specific_blog = Blog.objects.get(id=id)
    specific_blog.delete()
    
    return redirect('/blogs')



def update(request, id):
    specific_blog = Blog.objects.get(id=id)
    

    
    context = {
        'update_blog': specific_blog,
    }
    if request.method == "POST":
        newcontent = request.POST['new_content']
        newdate = request.POST['newdate']
        specific_blog.blog_content = newcontent
        specific_blog.date = newdate

        specific_blog.save()
        
        return redirect('/blogs')

    return render(request, "update.html", context)
    