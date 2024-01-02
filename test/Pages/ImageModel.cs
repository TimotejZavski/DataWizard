using System;
namespace test.Pages
{
    public class ImageModel
    {
        public string FilePath { get; set; }
        public string FileName { get; internal set; }

        public ImageModel()
        {
            FilePath = string.Empty; 
        }
    }
}

